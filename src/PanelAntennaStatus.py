# -*- coding: utf-8 -*-

import wx

class PanelAntennaStatus(wx.Panel):    
    
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent=parent)
        self.outerSizer = wx.BoxSizer(wx.VERTICAL)
        self.innerSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.innerSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.innerSizer3 = wx.BoxSizer(wx.HORIZONTAL)        
        self.antennasIcon = []
        self.antennasStatus = []
        
        for i in range(1,31):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer1.Add(self.antennasIcon[-1], 1, wx.EXPAND)
        for i in range(31,61):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer2.Add(self.antennasIcon[-1], 1, wx.EXPAND)
        for i in range(61,91):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer3.Add(self.antennasIcon[-1], 1, wx.EXPAND)
            
        self.outerSizer.Add(self.innerSizer1, 0, wx.EXPAND) 
        self.outerSizer.Add(self.innerSizer2, 0, wx.EXPAND)
        self.outerSizer.Add(self.innerSizer3, 0, wx.EXPAND)  
        self.SetSizerAndFit(self.outerSizer) 
            
    def createAntennaStatusAndIcon(self, index):
        self.antennasIcon.append(wx.StaticText(self, -1, label=str(index), \
                                           size=(18,20), \
                                           style=wx.ALIGN_CENTER | wx.BORDER_SIMPLE))
        self.antennasStatus.append(False)
        
    def refreshAntennas(self):
        index = 0
        for status in self.antennasStatus:
            if status:
                self.antennasIcon[index].SetBackgroundColour("green")                
            else:
                self.antennasIcon[index].SetBackgroundColour(wx.NullColour)
            index = index+1
            
                
    def toggleAntenna(self,antNmbr):
        i = antNmbr - 1
        #antenna = self.antennasIcon[i]
        if self.antennasStatus[i]:
            self.antennasStatus[i] = False            
        else:
            self.antennasStatus[i] = True
        self.refreshAntennas()
            
        

         
            
            
# app = wx.App(False)
# frame = wx.Frame(None)
# panel = PanelAntennaStatus(frame)
# panel.toggleAntenna(66)
# panel.toggleAntenna(66)
# #panel.refreshAntennas()
# 
# frame.Show()
#app.MainLoop()