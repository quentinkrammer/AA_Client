# -*- coding: utf-8 -*-

#import os
import wx
from wx._core import ID_ANY

class GUI_SendCmdList(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)      
        self.entries = []        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetMinSize((270,234))        
        self.SetSizer(self.sizer) 
    
    def addEntry(self,cmd):
        label = wx.Button(self, ID_ANY, label=cmd)
        self.entries.append(label)
        self.refreshList()
        
    def refreshList(self):        
        self.sizer.Add(self.entries[-1], 0, wx.EXPAND)
        #self.sizer.
        
#https://stackoverflow.com/questions/49922095/overlapping-widgets-controls-within-wxpython-boxsizer
        

