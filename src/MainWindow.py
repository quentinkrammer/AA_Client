# -*- coding: utf-8 -*-

import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent=None, title="AA_Client"):
        
        wx.Frame.__init__(self, parent, title=title, size=(1200,800))        
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Load a communication algorithm from a file")        
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.    
        
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        self.Show()    

 
    def OnExit(self,e):
        self.Close(True)  # Close the frame.
 
     
        
# app = wx.App(False)
# frame = MainWindow()
# panelButtons = PanelCommunicationButtons(frame)
# panelList = PanelCommunicationList(frame)
# receive = PanelReceive(frame)
#  
# sizer = wx.BoxSizer(wx.HORIZONTAL)
# sizer.Add(panelButtons)
# sizer.Add(panelList, 1, wx.EXPAND)
# sizer.Add(receive, 1, wx.EXPAND)
# 
# frame.SetSizerAndFit(sizer)
# app.MainLoop()
