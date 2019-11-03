# -*- coding: utf-8 -*-

import os
import wx

class GUI_BasicCmdBtn():
    def __init__(self):
        self.basicBtns  = []
        self.basicBtns.append( {
          "cmd": "ANT:ACT",          
          "numberOfInputValues": 1
        } )
        self.basicBtns.append( {
          "cmd": "ANT:DEACT",          
          "numberOfInputValues": 1
        } )
        self.basicBtns.append( {
          "cmd": "ANT:SWITCH",          
          "numberOfInputValues": 2
        } )
        self.basicBtns.append( {
          "cmd": "ANT:SWITCH:CONT",          
          "numberOfInputValues": 2
        } )
        self.basicBtns.append( {
          "cmd": "ANT:SWITCH:OFF",          
          "numberOfInputValues": 0
        } )
        self.basicBtns.append( {
          "cmd": "SYS:DIST",          
          "numberOfInputValues": 1
        } )
        self.basicBtns.append( {
          "cmd": "SYS:ANG",          
          "numberOfInputValues": 1
        } )
        self.basicBtns.append( {
          "cmd": "SYS:ON",          
          "numberOfInputValues": 0
        } )
        self.basicBtns.append( {
          "cmd": "SYS:OFF",          
          "numberOfInputValues": 0
        } )
        
    def appendButtons(self, frame):
        sizer_outerFrame = wx.BoxSizer(wx.VERTICAL)      
        for btns in self.basicBtns:
            sizer_innerFrame = wx.BoxSizer(wx.HORIZONTAL)
            button = wx.Button(frame, -1, btns["cmd"])
            button.SetMinSize((128,-1))
            sizer_innerFrame.Add(button, 0, wx.EXPAND)
            for i in range(0, btns["numberOfInputValues"]):                  
                control = wx.TextCtrl(frame, size=(20, -1))
                control.SetMaxLength(2)
                sizer_innerFrame.Add(control, 0, wx.EXPAND)            
            sizer_outerFrame.Add(sizer_innerFrame, 0, wx.EXPAND)            
        return sizer_outerFrame       
        

#b =  GUI_BasicCmdBtn()    
#print(b.basicBtns)

