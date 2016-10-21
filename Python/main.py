import signal # For trapping ctrl-c or SIGINT
import sys # For exiting program with exit code
import SerialHandler 
import TempHandler
import FileWriter
import Grapher
import time 

Serial_Handler = SerialHandler.SerialHandler() 
Temp_Handler = TempHandler.TempHandler() 
Humidity_Handler = TempHandler.TempHandler()     #Using TempHandler class for humidity 
Dewpoint_Handler = TempHandler.TempHandler()     #And dewpoint
File_Writer = FileWriter.FileWriter() 
Plotter = Grapher.Grapher(Serial_Handler.getStart_Time()) 

#Handling program exit. Closes serial connection.
#Also saves graph to pdf
def SIGINT_handler(signal, frame): 
        print('Quitting program!')
        Serial_Handler.close() 
        path = 'Logs\Log%s.csv'%(Serial_Handler.getStart_Time())
        Plotter.produceGraph(path) 
        sys.exit(0)
        
signal.signal(signal.SIGINT, SIGINT_handler)

#Perform the actions that happen every Out_Period
#Outputs the average temperature (stored in msg) over the Out_Period 
def onPeriod(): 
    global Start
    Start = time.time() 
    temp = Temp_Handler.getTempAve() 
    hmdty = Humidity_Handler.getTempAve()
    dwpnt = Dewpoint_Handler.getTempAve()
    Temp_Handler.resetTemps() 
    print ("%s    temp: %s   hmdty: %0.2f    dwpnt: %s" %(now, temp, hmdty, dwpnt)) 
    if(msg != "No temperature data"): 
        #File_Writer.writeToTxt(Serial_Handler.getStart_Time(), now, msg) 
        File_Writer.writeToCsv(Serial_Handler.getStart_Time(), now, temp, hmdty, dwpnt) 
        Plotter.plotData(float((time.time()-Serial_Handler.getStart_Time_Long())/3600), float(temp)) 
      
      
Start = time.time()             
Serial_Handler.syncToBoard()	    
#Main loop
while(1):               
    msg = Serial_Handler.readLine() 
    if(len(msg)>0):
        now= time.strftime("%Y-%m-%dT%H:%M:%S") 
        temp = Temp_Handler.extractTemp(msg)
        Humidity_Handler.recordTemp(Humidity_Handler.getWord(msg,1)) #Quick hack by using recordTemp instead of
        Dewpoint_Handler.recordTemp(Dewpoint_Handler.getWord(msg,2)) #making a recordHumidity
        
        dt = time.time() - Start
        if(dt >= Serial_Handler.getOut_Period()): 
            onPeriod() 
    Plotter.processEvents() #Also handles GUI events. Must be called frequently.
