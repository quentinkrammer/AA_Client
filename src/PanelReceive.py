# -*- coding: utf-8 -*-

import wx
# new shit
class PanelReceive(wx.Panel):
    def __init__( self, parent):        #, sizeC=(200,50)
        wx.Panel.__init__(self, parent=parent) #, size(-1, sizeY)
        label = wx.StaticText(self, -1, label="AA response: ")
        clearBtn = wx.Button(self, -1, label="Clear")
        self.text = wx.TextCtrl(self, size=(259,-1) , style=wx.TE_MULTILINE|wx.TE_READONLY)
        
        self.Bind(wx.EVT_BUTTON, self.onBtn, clearBtn)        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label,0, wx.ALIGN_CENTER)
        sizer.Add(self.text, 1, wx.EXPAND)
        sizer.Add(clearBtn, 0, wx.EXPAND)
                      
        self.SetSizerAndFit(sizer)
        
    def onBtn(self,e):
        self.text.Clear()

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