# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel
# from MainWindow import MainWindow
# from PanelCommunicationButtons import PanelCommunicationButtons

class PanelCommunicationList(wx.Panel):
    def __init__( self, parent):        #, sizeC=(200,50)
        wx.Panel.__init__(self, parent=parent) #, size(-1, sizeY)
        label = wx.StaticText(self, -1, label="Communication window")
        self.sendBtn =  wx.Button(self, label="Send")
        self.listElements = [] 
                
        self.list = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(-1 ,278), pos=(0,0), style=wx.SIMPLE_BORDER)
        self.list.SetupScrolling()
        self.listSizer = wx.BoxSizer(wx.VERTICAL)        

        self.list.SetSizer(self.listSizer)          

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(label,0, wx.ALIGN_CENTER)
        self.sizer.Add(self.list, 1, wx.EXPAND)
        self.sizer.Add(self.sendBtn, 0, wx.EXPAND)                
        self.SetSizerAndFit(self.sizer)
        #print("Size of PanelCommunicationButtons: " + str(self.GetSize()))
        
    def addToList(self, cmd):
        newEle = wx.Button(self.list, label=cmd)
        self.listElements.append(newEle)
        self.listSizer.Add(newEle, 0, wx.EXPAND)        
        self.list.Bind(wx.EVT_BUTTON, self.removeFromList, newEle)
        self.sizer.RecalcSizes() 
        
    def removeFromList(self, e):
        e.GetEventObject().Destroy()
        self.sizer.RecalcSizes() 
        
# app = wx.App(False)
# frame = MainWindow()
# panelButtons = PanelCommunicationButtons(frame)
# panelList = PanelCommunicationList(frame)
# 
# sizer = wx.BoxSizer(wx.HORIZONTAL)
# sizer.Add(panelButtons)
# sizer.Add(panelList, 1, wx.EXPAND)
# frame.SetSizerAndFit(sizer)
# 
# app.MainLoop()