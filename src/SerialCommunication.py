# -*- coding: utf-8 -*-

import serial

class SerialCommunication:    
    
    def __init__(self, baudrate=115200, port="COM16"):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.timeout = 1
        #self.ser.open()
 
    def readNextMsg(self):
        msg = ""
        endOfMsg = False
        while(True):
            byte = self.ser.read()
            char = byte.decode()        
            if char == "\n" or not char:
                break
            else:
                msg += char                
        return msg
    
    def parseCmd(self, cmd):
        self.ser.open()
        replies = []
        try:            
            cmd += "\n"
            self.ser.write(cmd.encode())
            while(True):
                msg = self.readNextMsg()                
                if not msg:
                    break
                replies.append(msg+"\n")
#                             
        except Exception as e:
            print(e)
            
        finally:   
            self.ser.close()        
            return replies
