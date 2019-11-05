# -*- coding: utf-8 -*-

import wx

class PanelReceive(wx.Panel):
    def __init__( self, parent):        #, sizeC=(200,50)
        wx.Panel.__init__(self, parent=parent) #, size(-1, sizeY)
        label = wx.StaticText(self, -1, label="AA response: ")
        text = wx.TextCtrl(self, size=(259,-1) , style=wx.TE_MULTILINE|wx.TE_READONLY)        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label,0, wx.ALIGN_CENTER)
        sizer.Add(text, 1, wx.EXPAND)
                      
        self.SetSizerAndFit(sizer)

# app = wx.App(False)        
# frame = wx.Frame(None)
# frame.Show()
# 
# reply = PanelReceive(frame)
# 
# sizer = wx.BoxSizer(wx.HORIZONTAL)
# sizer.Add(reply, 1, wx.EXPAND)
# frame.SetSizerAndFit(sizer)

#app.MainLoop()