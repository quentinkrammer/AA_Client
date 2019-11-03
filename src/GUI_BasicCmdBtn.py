# -*- coding: utf-8 -*-

import os
import wx
from wx._core import ID_ANY

class GUI_BasicCmdBtn():
    def __init__(self, frame):
        self.frame = frame
        self.basicCmds  = []
        self.basicCmds.append( {
          "cmd": "ANT:ACT",          
          "numberOfInputValues": 1
        } )
        self.basicCmds.append( {
          "cmd": "ANT:DEACT",          
          "numberOfInputValues": 1
        } )
        self.basicCmds.append( {
          "cmd": "ANT:SWITCH",          
          "numberOfInputValues": 2
        } )
        self.basicCmds.append( {
          "cmd": "ANT:SWITCH:CONT",          
          "numberOfInputValues": 2
        } )
        self.basicCmds.append( {
          "cmd": "ANT:SWITCH:OFF",          
          "numberOfInputValues": 0
        } )
        self.basicCmds.append( {
          "cmd": "SYS:DIST",          
          "numberOfInputValues": 1
        } )
        self.basicCmds.append( {
          "cmd": "SYS:ANG",          
          "numberOfInputValues": 1
        } )
        self.basicCmds.append( {
          "cmd": "SYS:ON",          
          "numberOfInputValues": 0
        } )
        self.basicCmds.append( {
          "cmd": "SYS:OFF",          
          "numberOfInputValues": 0
        } )
        self.sizer = wx.BoxSizer(wx.VERTICAL) 
        self.menuItems = []
        self.iniBasicCmdMenu()
                
    def iniBasicCmdMenu(self):        
        for cmds in self.basicCmds:
            sizer = wx.BoxSizer(wx.HORIZONTAL)            
            button = wx.Button(self.frame, ID_ANY, cmds["cmd"])
            button.requiresTxtInput = []            
            #button.SetToolTip("sdfsdfsd")
            #button.SetHelpText("rgergerg")
            button.SetMinSize((128,-1))
            sizer.Add(button, 0, wx.EXPAND)
            self.menuItems.append([])
            self.menuItems[-1].append(button)
            for x in range(0, cmds["numberOfInputValues"]):                                
                control = wx.TextCtrl(self.frame, size=(20, -1))
                control.SetMaxLength(2)                
                sizer.Add(control, 0, wx.EXPAND) 
                #self.menuItems[-1].append(control)
                button.requiresTxtInput.append(control)                           
            self.sizer.Add(sizer, 0, wx.EXPAND)            
             
        

