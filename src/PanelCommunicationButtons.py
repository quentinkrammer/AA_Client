# -*- coding: utf-8 -*-

import wx

class PanelCommunicationButtons(wx.Panel):
    def __init__( self, parent ):
        wx.Panel.__init__(self, parent=parent)        
        
        self.btn0 = wx.Button(self, -1, "IDLE")
        self.btn1 = wx.Button(self, -1, "ANT:ACT")
        self.btn2 = wx.Button(self, -1, "ANT:DEACT")
        self.btn3 = wx.Button(self, -1, "ANT:SWITCH")
        self.btn4 = wx.Button(self, -1, "ANT:SWITCH:CONT")
        self.btn5 = wx.Button(self, -1, "ANT:SWITCH:OFF")
        self.btn6 = wx.Button(self, -1, "SYS:DIST")
        self.btn7 = wx.Button(self, -1, "SYS:ANG")
        self.btn8 = wx.Button(self, -1, "SYS:ON")
        self.btn9 = wx.Button(self, -1, "SYS:OFF")
        self.btn10 = wx.Button(self, -1, "SEQUENZ")
        self.btn11 = wx.Button(self, -1, "COMBINE")
        
        self.btn3.Disable()
        self.btn4.Disable() 
        self.btn5.Disable() 
        self.btn6.Disable() 
        self.btn7.Disable() 
        self.btn8.Disable() 
        self.btn9.Disable()              
        
        self.txt01 = wx.TextCtrl(self, size=(20, -1))
        self.txt11 = wx.TextCtrl(self, size=(20, -1))
        self.txt21 = wx.TextCtrl(self, size=(20, -1))
        self.txt31 = wx.TextCtrl(self, size=(20, -1))
        self.txt32 = wx.TextCtrl(self, size=(20, -1))
        self.txt41 = wx.TextCtrl(self, size=(20, -1))
        self.txt42 = wx.TextCtrl(self, size=(20, -1))
        self.txt61 = wx.TextCtrl(self, size=(20, -1))
        self.txt71 = wx.TextCtrl(self, size=(20, -1))
        self.txt10_1 = wx.TextCtrl(self, size=(20, -1))
        self.txt10_2 = wx.TextCtrl(self, size=(20, -1))
        self.txt10_3 = wx.TextCtrl(self, size=(20, -1))
        self.txt10_4 = wx.TextCtrl(self, size=(20, -1))
        self.txt11_1 = wx.TextCtrl(self, size=(20, -1))
        self.txt11_2 = wx.TextCtrl(self, size=(20, -1))
        
        self.txt01.SetMaxLength(4)
        self.txt11.SetMaxLength(2)
        self.txt21.SetMaxLength(2)
        self.txt31.SetMaxLength(2)
        self.txt32.SetMaxLength(2)
        self.txt41.SetMaxLength(2)
        self.txt42.SetMaxLength(2)
        self.txt61.SetMaxLength(10)
        self.txt71.SetMaxLength(10)
        self.txt10_1.SetMaxLength(2)
        self.txt10_2.SetMaxLength(2)
        self.txt10_3.SetMaxLength(2)
        self.txt10_4.SetMaxLength(2)
        self.txt11_1.SetMaxLength(2)
        self.txt11_2.SetMaxLength(2)
        
        self.btn0.requiredInput = [self.txt01]        
        self.btn1.requiredInput = [self.txt11]
        self.btn2.requiredInput = [self.txt21]
        self.btn3.requiredInput = [self.txt31, self.txt32]
        self.btn4.requiredInput = [self.txt41, self.txt42]
        self.btn6.requiredInput = [self.txt61]
        self.btn7.requiredInput = [self.txt71]
        self.btn10.requiredInput = [self.txt10_1, self.txt10_2, self.txt10_3, self.txt10_4]
        self.btn11.requiredInput = [self.txt11_1, self.txt11_2]      

        self.grid = wx.GridBagSizer(hgap=10, vgap=4)
        
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
        self.grid.Add(self.btn10, (10,0))
        self.grid.Add(self.btn11, (11,0))
        
        self.grid.Add(self.txt01, (0,1))
        self.grid.Add(self.txt11, (1,1))
        self.grid.Add(self.txt21, (2,1))
        self.grid.Add(self.txt31, (3,1))
        self.grid.Add(self.txt32, (3,2))
        self.grid.Add(self.txt41, (4,1))
        self.grid.Add(self.txt42, (4,2))
        self.grid.Add(self.txt61, (6,1))
        self.grid.Add(self.txt71, (7,1))
        self.grid.Add(self.txt10_1, (10,1))
        self.grid.Add(self.txt10_2, (10,2))
        self.grid.Add(self.txt10_3, (10,3))
        self.grid.Add(self.txt10_4, (10,4))
        self.grid.Add(self.txt11_1, (11,1))
        self.grid.Add(self.txt11_2, (11,2))
        
        self.SetSizerAndFit(self.grid)
        
