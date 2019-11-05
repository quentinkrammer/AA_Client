# -*- coding: utf-8 -*-

import wx
import wx.lib.scrolledpanel
# from MainWindow import MainWindow
# from PanelCommunicationButtons import PanelCommunicationButtons

class PanelCommunicationList(wx.Panel):
    def __init__( self, parent):        #, sizeC=(200,50)
        wx.Panel.__init__(self, parent=parent) #, size(-1, sizeY)
        label = wx.StaticText(self, -1, label="Communication window")
        sendBtn =  wx.Button(self, label="Send") 
                
        self.list = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(-1 ,278), pos=(0,0), style=wx.SIMPLE_BORDER)
        self.list.SetupScrolling()
        self.listSizer = wx.BoxSizer(wx.VERTICAL)
        
        
        listEle1 = wx.Button(self.list, label="abcsabcsdrwerwerwabcsdrwerwerwdrwerwerw")
        listEle2 = wx.Button(self.list)
        listEle3 = wx.Button(self.list)
        listEle4 = wx.Button(self.list)
        listEle5 = wx.Button(self.list)
        listEle6 = wx.Button(self.list)
        listEle7 = wx.Button(self.list)
        listEle8 = wx.Button(self.list)
        listEle9 = wx.Button(self.list)
        listEle10 = wx.Button(self.list)
        listEle11 = wx.Button(self.list)
        listEle12 = wx.Button(self.list)
        listEle13 = wx.Button(self.list)
        
        self.listSizer.Add(listEle1, 0, wx.EXPAND) 
        self.listSizer.Add(listEle2, 0, wx.EXPAND)
        self.listSizer.Add(listEle3, 0, wx.EXPAND)
        self.listSizer.Add(listEle4, 0, wx.EXPAND)
        self.listSizer.Add(listEle5, 0, wx.EXPAND)
        self.listSizer.Add(listEle6, 0, wx.EXPAND)
        self.listSizer.Add(listEle7, 0, wx.EXPAND)
        self.listSizer.Add(listEle8, 0, wx.EXPAND)
        self.listSizer.Add(listEle9, 0, wx.EXPAND)
        self.listSizer.Add(listEle10, 0, wx.EXPAND)
        self.listSizer.Add(listEle11, 0, wx.EXPAND)
        self.listSizer.Add(listEle12, 0, wx.EXPAND)
        self.listSizer.Add(listEle13, 0, wx.EXPAND)
        self.list.SetSizer(self.listSizer)          

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label,0, wx.ALIGN_CENTER)
        sizer.Add(self.list, 1, wx.EXPAND)
        sizer.Add(sendBtn, 0, wx.EXPAND)                
        self.SetSizerAndFit(sizer)
        #print("Size of PanelCommunicationButtons: " + str(self.GetSize()))
        
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