# -*- coding: utf-8 -*-

import wx

class PanelAntennaStatus(wx.Panel):    
    
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent=parent)
        self.outerSizer = wx.BoxSizer(wx.VERTICAL)
        self.innerSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.innerSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.innerSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.innerSizer4 = wx.BoxSizer(wx.HORIZONTAL)        
        self.antennaButtons = []
        self.antennasStatus = []
        
        for i in range(0,30):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer1.Add(self.antennaButtons[-1], 1, wx.EXPAND)
        for i in range(30,60):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer2.Add(self.antennaButtons[-1], 1, wx.EXPAND)
        for i in range(60,90):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer3.Add(self.antennaButtons[-1], 1, wx.EXPAND)
        for i in range(90,96):
            self.createAntennaStatusAndIcon(i)
            self.innerSizer4.Add(self.antennaButtons[-1], 1, wx.EXPAND)
            
        self.outerSizer.Add(self.innerSizer1, 0, wx.EXPAND) 
        self.outerSizer.Add(self.innerSizer2, 0, wx.EXPAND)
        self.outerSizer.Add(self.innerSizer3, 0, wx.EXPAND)
        self.outerSizer.Add(self.innerSizer4, 0, wx.EXPAND)    
        self.SetSizerAndFit(self.outerSizer) 
            
    def createAntennaStatusAndIcon(self, index):
        self.antennaButtons.append(wx.Button(self, -1, label=str(index), \
                                           size=(18,20), \
                                           style=wx.ALIGN_CENTER | wx.BORDER_SIMPLE))
        self.antennasStatus.append(False)
        
    def refreshAntennas(self):
        index = 0
        for status in self.antennasStatus:
            if status:
                self.antennaButtons[index].SetBackgroundColour("green")                
            else:
                self.antennaButtons[index].SetBackgroundColour(wx.NullColour)
            index = index+1
            
                
    def toggleAntenna(self,antNmbr):
        i = int(antNmbr)
        if self.antennasStatus[i]:
            cmd =self.getCmd(antNmbr)
            self.antennasStatus[i] = False
        else:
            cmd = self.getCmd(antNmbr)
            self.antennasStatus[i] = True
        self.refreshAntennas()
        return cmd
    
    def getCmd(self,antNmbr):
        i = int(antNmbr)
        if self.antennasStatus[i]:
            cmd = "ANT:DEACT "+antNmbr            
        else:
            cmd = "ANT:ACT "+antNmbr 
        return cmd           
            
            
# app = wx.App(False)
# frame = wx.Frame(None)
# panel = PanelAntennaStatus(frame)
# panel.toggleAntenna(66)
# #panel.toggleAntenna(66)
# panel.refreshAntennas()
# 
# frame.Show()
# app.MainLoop()