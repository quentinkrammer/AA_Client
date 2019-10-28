# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:12:44 2019
@author: ip15oheg
"""
import serial
 
def readNextMsg():
    msg = ""
    endOfMsg = False
    while(not endOfMsg):
        char = ser.read().decode()        
        if char == "\n":
            endOfMsg = True
        else:
            msg += char  
    return msg

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM16'
ser.timeout = 0.500
ser.open()

try:
    cmd = "SYS:OFF"
    cmd += "\n"
    ser.write(cmd.encode())
    echo = readNextMsg()
    print(echo)
    reply = readNextMsg()
    print(reply)
    #print(readNextMsg())
    #print(readNextMsg())

except Exception as e:
    print(e)
    
finally:   
    ser.close()
