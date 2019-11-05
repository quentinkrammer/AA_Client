# -*- coding: utf-8 -*-

import wx
import os
from PanelCommunicationButtons import PanelCommunicationButtons
from PanelCommunicationList import PanelCommunicationList
from PanelReceive import PanelReceive
from MainWindow import MainWindow

app = wx.App(False)
frame = MainWindow()
panelButtons = PanelCommunicationButtons(frame)
panelList = PanelCommunicationList(frame)
receive = PanelReceive(frame)
 
sizer = wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(panelButtons)
sizer.Add(panelList, 1, wx.EXPAND)
sizer.Add(receive, 1, wx.EXPAND)

frame.SetSizerAndFit(sizer)
app.MainLoop()

