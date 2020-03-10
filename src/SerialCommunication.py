# -*- coding: utf-8 -*-

import serial

class SerialCommunication:    
    
    def __init__(self, baudrate=115200, port="COM16"):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        self.ser.timeout = 1
        self.ser.open()
        
    def __del__(self):
        self.ser.close()
    
    def parseCmd(self, cmd):        
        replies = []
        try:            
            cmd += "\n"
            self.ser.write(cmd.encode())
            while(True):
                msg = self.ser.readline().decode()                
                if not msg:
                    break
                replies.append(msg)
                             
        except Exception as e:
            print(e)
            
        finally:                  
            return replies

