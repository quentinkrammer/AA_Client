# -*- coding: utf-8 -*-

import wx
import os
# from PanelCommunicationButtons import PanelCommunicationButtons
# from PanelCommunicationList import PanelCommunicationList
# from PanelReceive import PanelReceive

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
       
#         # Events.
#         self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
#         
#         self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
#         for btns in cmdMenu.menuItems:
#             self.Bind(wx.EVT_BUTTON, self.onBasicCmdBtns, btns[0])         

        #Layout sizers
#         self.SetSizer(self.outerSizer)
#         self.SetAutoLayout(1)
#         self.outerSizer.Fit(self)
 
        
#     def onBasicCmdBtns(self,e):
#         btn = e.GetEventObject()
#         cmd = btn.GetLabel()
#         for txtInput in btn.requiresTxtInput:
#             cmd = cmd  + " " + txtInput.GetValue()
#         self.cmdList.addEntry(cmd)        
 
    def OnExit(self,e):
        self.Close(True)  # Close the frame.
 
#     def OnOpen(self,e):
#         """ Open a file"""
#         dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
#         if dlg.ShowModal() == wx.ID_OK:
#             self.filename = dlg.GetFilename()
#             self.dirname = dlg.GetDirectory()
#             f = open(os.path.join(self.dirname, self.filename), 'r')
#             self.control.SetValue(f.read())
#             f.close()
#         dlg.Destroy()

     
        
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
