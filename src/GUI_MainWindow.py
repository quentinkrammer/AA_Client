# -*- coding: utf-8 -*-

import wx
import os
from GUI_BasicCmdBtn import GUI_BasicCmdBtn
from GUI_SendCmdList import GUI_SendCmdList

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname=''
        # A "-1" in the size parameter instructs wxWidgets to use the default size.
        # In this case, we select 200px width and the default height.
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.communicationLog = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to edit")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        
        cmdMenu = GUI_BasicCmdBtn(self)
        self.cmdList = GUI_SendCmdList(self)
       
        # Events.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        for btns in cmdMenu.menuItems:
            self.Bind(wx.EVT_BUTTON, self.onBasicCmdBtns, btns[0])         

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(cmdMenu.sizer, 0, wx.EXPAND)
        self.sizer.Add(self.cmdList, 0, wx.EXPAND)
        
        self.outerSizer = wx.BoxSizer(wx.VERTICAL)
        self.outerSizer.Add(self.sizer, 0, wx.EXPAND)
        self.outerSizer.Add(self.communicationLog, 0, wx.EXPAND)
        

        #Layout sizers
        self.SetSizer(self.outerSizer)
        self.SetAutoLayout(1)
        self.outerSizer.Fit(self)
        self.Show()
        
    def onBasicCmdBtns(self,e):
        btn = e.GetEventObject()
        cmd = btn.GetLabel()
        for txtInput in btn.requiresTxtInput:
            cmd = cmd  + " " + txtInput.GetValue()
        self.cmdList.addEntry(cmd)        
        

    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " A sample editor \n in wxPython", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "AA Client")
app.MainLoop()
