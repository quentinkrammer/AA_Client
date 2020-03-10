# -*- coding: utf-8 -*-

import wx
import os
import time
import re
import threading
import socket
from SerialCommunication import SerialCommunication
from PanelCommunicationButtons import PanelCommunicationButtons
from PanelCommunicationList import PanelCommunicationList
from PanelAntennaStatus import PanelAntennaStatus
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

def onQuickBtn(e):
    nmbr = e.GetEventObject().GetLabel()
    cmd = panelStatus.getCmd(nmbr)
    panelList.clearList2()
    panelList.addToList(cmd)
    onSend(e)
    
def onSend(e):
    for listeEle in panelList.list.GetChildren():
        cmd = listeEle.GetLabel()
        if not "IDLE" in cmd:
            replies = ser.parseCmd(cmd)
            ######Central Data Collection ######### 
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall( (cmd).encode() ) 
            ######Central Data Collection #########  
            nmbr = re.search(r'\d+', cmd).group() 
            c = panelStatus.toggleAntenna(nmbr)
            for reply in replies:
                receive.text.AppendText(reply)
            if len(replies) == 0:
                receive.text.AppendText("AA is not responding.\nTry restarting this program to reset the serial connection.\n")
        else: 
            handleIdleBtn(listeEle.GetLabel())
        frame.Update() 
    panelList.clearList2()
            
def handleIdleBtn(label):
    digits = re.findall(r'\d+', label)
    seconds = int(digits[0])
    receive.text.AppendText("Idle for "+str(seconds)+" seconds.\n")
    time.sleep(seconds)

def onCombine(e):
    btn = e.GetEventObject()
    nmbr = int(btn.requiredInput[0].GetValue())
    idle = btn.requiredInput[1].GetValue()
    for i in range(0,96):
        if ( i != nmbr ):
            panelList.addToList("ANT:ACT "+str(i))
            if idle:
                panelList.addToList("IDLE "+str(idle))
            panelList.addToList("ANT:DEACT "+str(i)) 
        i += 1
    
    
def onSequenz(e):
    activate = "ANT:ACT "
    deactivate = "ANT:DEACT "
    idle = "IDLE "
    btn = e.GetEventObject()
    if btn.requiredInput[0].GetValue() == '':
        min = 1
    else:
        min = int(btn.requiredInput[0].GetValue())
    if btn.requiredInput[1].GetValue() == '':
        max = 91
    else:
        max = int(btn.requiredInput[1].GetValue()) + 1
    if btn.requiredInput[2].GetValue() == '':
        stepSize = 1
    else:
        stepSize = int(btn.requiredInput[2].GetValue())
    if btn.requiredInput[3].GetValue() == '':
        idleTime = 0
    else:
        idleTime = int(btn.requiredInput[3].GetValue())
    
    panelList.addToList(activate+str(min))    
    if idleTime == 0:        
        for i in range(min, max, stepSize):
            if i+stepSize < max:        
                panelList.addToList(deactivate+str(i))                          
                panelList.addToList(activate+str(i+stepSize))            
    else:        
        for i in range(min, max, stepSize):
            if i+stepSize < max:  
                panelList.addToList(idle+str(idleTime))
                panelList.addToList(deactivate+str(i))                           
                panelList.addToList(activate+str(i+stepSize)) 
            

HOST = '127.0.0.1'  
PORT = 12121       
   
ser = SerialCommunication()

app = wx.App(False)
frame = MainWindow()
panelButtons = PanelCommunicationButtons(frame)
panelList = PanelCommunicationList(frame)
receive = PanelReceive(frame)
panelStatus = PanelAntennaStatus(frame)
 
sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(panelButtons)
sizer.Add(panelList, 1, wx.EXPAND)
sizer.Add(receive, 1, wx.EXPAND)

sizer2 = wx.BoxSizer(wx.VERTICAL)
sizer2.Add(sizer, 1, wx.EXPAND)
sizer2.Add(panelStatus, 0, wx.EXPAND)

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
frame.Bind(wx.EVT_BUTTON, onSequenz, panelButtons.btn10)
frame.Bind(wx.EVT_BUTTON, onCombine, panelButtons.btn11)
frame.Bind(wx.EVT_BUTTON, onSend, panelList.sendBtn)
for i in range(0,96):
    frame.Bind(wx.EVT_BUTTON, onQuickBtn, panelStatus.antennaButtons[i])

frame.SetSizerAndFit(sizer2)
app.MainLoop()
