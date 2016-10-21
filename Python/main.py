import signal # For trapping ctrl-c or SIGINT
import sys # For exiting program with exit code
import SerialHandler 
import TempHandler
import FileWriter
import Emailer
import Grapher
import time 

Serial_Handler = SerialHandler.SerialHandler() 
Temp_Handler = TempHandler.TempHandler() 
File_Writer = FileWriter.FileWriter() 
Failure_Emailer = Emailer.Emailer() 
Plotter = Grapher.Grapher(Serial_Handler.getStart_Time()) 

#Handling program exit. Closes serial connection.
#Also saves graph to pdf
def SIGINT_handler(signal, frame): 
        print('Quitting program!')
        Serial_Handler.SendMessages = False
        while("Fets_Off" not in Serial_Handler.readLine()): 
            Serial_Handler.ser.write("Mosfets_Off")
            print "waiting for Mosfets to turn off"
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
    msg = Temp_Handler.getTempAve() 
    Temp_Handler.resetTemps() 
    print ("%s    %s" %(now, msg)) 
    if(msg != "No temperature data"): 
        #File_Writer.writeToTxt(Serial_Handler.getStart_Time(), now, msg) 
        File_Writer.writeToCsv(Serial_Handler.getStart_Time(), now, msg) 
        Plotter.plotData(float((time.time()-Serial_Handler.getStart_Time_Long())/3600), float(msg)) 
      
      
Start = time.time()             
Serial_Handler.syncToBoard()	    
#Main loop
while(1):          
    Serial_Handler.writeLine("Mosfets_On")  #Tell arduino to start ramping MOSFETS up        
    msg = Serial_Handler.readLine() 
    if("failure" in str(msg) and Failure_Emailer.getEmailSent() == False): 
        Failure_Emailer.sendFailureEmail(Temp_Handler.getBestTemp()) 
        
    if(len(msg)>0 and "failure" not in str(msg) and "Fets_Off" not in str(msg)):
        now= time.strftime("%Y-%m-%dT%H:%M:%S") 
        msg = Temp_Handler.extractTemp(msg)
    
        dt = time.time() - Start
        if(dt >= Serial_Handler.getOut_Period()): 
            onPeriod() 
    Plotter.processEvents() #Also handles GUI events. Must be called frequently.
