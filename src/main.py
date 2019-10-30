# -*- coding: utf-8 -*-

import wx
import SerialCommunication

#Create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()

ser = SerialCommunication.SerialCommunication()
replies = ser.parseCmd("ANT:ACT 10")
for reply in replies:
    print(reply)