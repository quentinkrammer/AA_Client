from datetime import datetime

class Logger(object):

    def __init__(self):
        self.filename = datetime.now()
        #filename = filename.replace(microsecond=0)
        self.filename = str(self.filename)
        self.filename = self.filename.replace(":", "-")
        self.filename = self.filename.replace(" ", "_")
        self.filename = self.filename+".txt"
        self.f = open(self.filename, "w")
        self.f.close()
        
    def logAction(self, msg):       
            self.f = open(self.filename, "a")
            timestamp = str(datetime.now())
            timestamp += " & "            
            self.f.write(timestamp)
            self.f.write(msg+"\n")
            self.f.close()
        