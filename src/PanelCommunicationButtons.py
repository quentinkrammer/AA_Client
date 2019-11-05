# -*- coding: utf-8 -*-

import wx

class PanelCommunicationButtons(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent=parent)        
        
        self.btn0 = wx.Button(self, -1, "SILENT")
        self.btn1 = wx.Button(self, -1, "ANT:ACT")
        self.btn2 = wx.Button(self, -1, "ANT:DEACT")
        self.btn3 = wx.Button(self, -1, "ANT:SWITCH")
        self.btn4 = wx.Button(self, -1, "ANT:SWITCH:CONT")
        self.btn5 = wx.Button(self, -1, "ANT:SWITCH:OFF")
        self.btn6 = wx.Button(self, -1, "SYS:DIST")
        self.btn7 = wx.Button(self, -1, "SYS:ANG")
        self.btn8 = wx.Button(self, -1, "SYS:ON")
        self.btn9 = wx.Button(self, -1, "SYS:OFF")      
        
        
        self.txt01 = wx.TextCtrl(self, size=(20, -1))
        self.txt11 = wx.TextCtrl(self, size=(20, -1))
        self.txt21 = wx.TextCtrl(self, size=(20, -1))
        self.txt31 = wx.TextCtrl(self, size=(20, -1))
        self.txt32 = wx.TextCtrl(self, size=(20, -1))
        self.txt41 = wx.TextCtrl(self, size=(20, -1))
        self.txt42 = wx.TextCtrl(self, size=(20, -1))
        self.txt61 = wx.TextCtrl(self, size=(20, -1))
        self.txt71 = wx.TextCtrl(self, size=(20, -1))
        
        self.txt01.SetMaxLength(2)
        self.txt11.SetMaxLength(2)
        self.txt21.SetMaxLength(2)
        self.txt31.SetMaxLength(2)
        self.txt32.SetMaxLength(2)
        self.txt41.SetMaxLength(2)
        self.txt42.SetMaxLength(2)
        self.txt61.SetMaxLength(2)
        self.txt71.SetMaxLength(2)
        
        self.btn0.requiredInput = [self.txt01]
        self.btn1.requiredInput = [self.txt11]
        self.btn2.requiredInput = [self.txt21]
        self.btn3.requiredInput = [self.txt31, self.txt32]
        self.btn4.requiredInput = [self.txt41, self.txt42]
        self.btn0.requiredInput = [self.txt61]
        self.btn0.requiredInput = [self.txt71]      

        self.grid = wx.GridBagSizer(hgap=9, vgap=2)
        
        self.grid.Add(self.btn0, (0,0))                      
        self.grid.Add(self.btn1, (1,0))
        self.grid.Add(self.btn2, (2,0))
        self.grid.Add(self.btn3, (3,0))
        self.grid.Add(self.btn4, (4,0))
        self.grid.Add(self.btn5, (5,0))
        self.grid.Add(self.btn6, (6,0))
        self.grid.Add(self.btn7, (7,0))
        self.grid.Add(self.btn8, (8,0))
        self.grid.Add(self.btn9, (9,0))
        
        self.grid.Add(self.txt01, (0,1))
        self.grid.Add(self.txt11, (1,1))
        self.grid.Add(self.txt21, (2,1))
        self.grid.Add(self.txt31, (3,1))
        self.grid.Add(self.txt32, (3,2))
        self.grid.Add(self.txt41, (4,1))
        self.grid.Add(self.txt42, (4,2))
        self.grid.Add(self.txt61, (6,1))
        self.grid.Add(self.txt71, (7,1))
        
        self.SetSizerAndFit(self.grid)
        print("Size of PanelCommunicationButtons: " + str(self.GetSize()))
        
# app = wx.App(False)
# frame = wx.Frame(None)
# panel = PanelCommunicationButtons(frame)
# frame.Show()
# app.MainLoop()