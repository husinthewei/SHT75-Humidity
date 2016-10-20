import time
import serial.tools.list_ports
import serial
class SerialHandler:
    
    #Records time program started 
    #For file name + documents + graph
    def __init__(self):
        self.Start_Time = time.strftime("%Y%m%dT%H%M%S") 
        self.Start_Time_Long = time.time() 
        self.createConnection()
        self.SendMessages = True
        self.promptOutputPeriod() 
      
    #Having user select the correct COM port for the Arduino  
    #Also creates connection with that COM port
    def createConnection(self):
        port_names=[]		
        a=serial.tools.list_ports.comports()
        for w in a:
            port_names.append(w.device)
    
        port_names.sort()
        print('\nDetected the following serial ports:\nDon\'t choose /dev/ttyAMA0.')
        i=0
        for w in port_names:
            print('%d) %s' %(i,w))
            i=i+1
        total_ports=i 
        user_port_selection=input('\nSelect port: (0,1,2...)    ')
        if (int(user_port_selection)>=total_ports):
            print 'Port not in range'
            exit(1)
        self.ser=serial.Serial(port=port_names[int(user_port_selection)],baudrate=9600,timeout=1)
    
    #Having user select how frequently to output data   
    def promptOutputPeriod(self):
        self.Out_Period = 0
        while(self.Out_Period <0.1): 
            self.Out_Period = input('Output data how often(seconds)? Minimum 0.1s    ')
        
    #Makes sure this script does not start in the middle of one of the Arduino output lines
    def syncToBoard(self):
        mycmd = ""
        while(mycmd != "\n"):
            mycmd=self.ser.read() 
            
    #Reads and returns a line of the arduino output        
    def readLine(self): 
        msg = ""
        mycmd = ""
        try:
            while(mycmd != "\n"): 
                msg += mycmd
                mycmd=self.ser.read()
        except Exception:
            print "Serial Error"  
        return msg
    
    def writeLine(self, msg):
        if self.SendMessages:
            self.ser.write(msg)
            
    #Close serial connection
    def close(self): 
        self.ser.close()
    
    def getOut_Period(self):
        return self.Out_Period
    def getStart_Time(self):
        return self.Start_Time
    def getStart_Time_Long(self):
        return self.Start_Time_Long
        