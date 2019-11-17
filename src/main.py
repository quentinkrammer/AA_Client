# -*- coding: utf-8 -*-

import wx
import os
import time
import re
from SerialCommunication import SerialCommunication
from PanelCommunicationButtons import PanelCommunicationButtons
from PanelCommunicationList import PanelCommunicationList
from PanelReceive import PanelReceive
from MainWindow import MainWindow

def onBtn(e):
    btn = e.GetEventObject()        
    cmd = btn.GetLabel()        
    if hasattr(btn, 'requiredInput'):                   
        for values in btn.requiredInput:
            value = values.GetValue()
            if value == '':
                wx.MessageBox("Values missing!")
                return;                                           
            cmd = cmd  + " " + values.GetValue()                   
    panelList.addToList(cmd)
    
def onSend(e):
    for listeEle in panelList.list.GetChildren():
        cmd = listeEle.GetLabel()
        if not "IDLE" in cmd: 
            replies = ser.parseCmd(listeEle.GetLabel())        
            for reply in replies:
                receive.text.AppendText(reply)
            if len(replies) == 0:
                receive.text.AppendText("AA is not responding.\nTry restarting this program to reset the serial connection.\n")
        else: 
            handleIdleBtn(listeEle.GetLabel())
            
def handleIdleBtn(label):
    digits = re.findall(r'\d+', label)
    seconds = int(digits[0])
    receive.text.AppendText("Idle for "+str(seconds)+" seconds.\n")
    time.sleep(seconds)
        
   
ser = SerialCommunication()

app = wx.App(False)
frame = MainWindow()
panelButtons = PanelCommunicationButtons(frame)
panelList = PanelCommunicationList(frame)
receive = PanelReceive(frame)
 
sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(panelButtons)
sizer.Add(panelList, 1, wx.EXPAND)
sizer.Add(receive, 1, wx.EXPAND)

frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn0)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn1)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn2)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn3)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn4)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn5)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn6)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn7)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn8)
frame.Bind(wx.EVT_BUTTON, onBtn, panelButtons.btn9)

frame.Bind(wx.EVT_BUTTON, onSend, panelList.sendBtn)

frame.SetSizerAndFit(sizer)
app.MainLoop()
