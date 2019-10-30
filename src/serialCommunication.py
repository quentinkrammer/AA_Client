# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:12:44 2019
@author: ip15oheg
"""
import serial

class serialCommunication:    
    
    def __init__(self, baudrate=115200, port="COM16"):
        self.ser = serial.Serial()
        self.baudrate = baudrate
        self.port = port
        #ser.timeout = 0.500
        self.ser.open()
 
    def readNextMsg(self):
        msg = ""
        endOfMsg = False
        while(not endOfMsg):
            char = self.ser.read().decode()        
            if char == "\n":
                endOfMsg = True
            else:
                msg += char  
        return msg
    
    def parseCmd(self, cmd):
        replies = []
        try:            
            cmd += "\n"
            self.ser.write(cmd.encode())
            if "ANT:ACT" in cmd:
                replies.append (self.readNextMsg(self))  #echo      
                replies.append (self.readNextMsg(self)) 
            elif "" in cmd:
                replies.append (self.readNextMsg(self))  #echo         
                replies.append (self.readNextMsg(self))
                replies.append (self.readNextMsg(self)) 
            else:
                replies.append (self.readNextMsg(self))  #echo         
                replies.append (self.readNextMsg(self))
                replies.append (self.readNextMsg(self))
                replies.append (self.readNextMsg(self))


    
        except Exception as e:
            print(e)
            
        finally:   
            self.ser.close()        
            return replies

    
    
        
    #This line was added in eclipse
