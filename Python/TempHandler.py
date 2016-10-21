class TempHandler:
    
    #Temp tuple stores temperatures for average calculations
    def __init__(self):
        self.Temps = ()
        self.LastTempKnown = 22 
    
    def getLastTempKnown(self):
        return self.LastTempKnown
    def getTemps(self):
        return self.Temps        
    def setTemps(self, temps):
        self.Temps = temps      
        
    #Records data to tuple for average calculations.
    def recordTemp(self, temp): 
        try: 
            self.Temps = self.Temps + (float(temp),) 
        except:
            pass      
            
    #Clears the tuple for new average calculations        
    def resetTemps(self):
        self.Temps = () 
   
    #Calculate the average from the data
    def getTempAve(self): 
        if(len(self.Temps) > 0):
            sum = 0
            for i in self.Temps:
                sum += i
            ave = (sum / len(self.Temps))
            self.LastTempKnown = ave
            return ave  
        else:
            return "No temperature data"
            
    #returns the best temperature to notify. Used for quick email
    def getBestTemp(self):
        temp = "unknown"
        if(len(self.Temps) > 0):
            temp = str(self.getTempAve())
        elif(len(str(self.LastTempKnown)) > 0):
            temp = str(self.LastTempKnown)
        return temp
            
    #Extracting temperature from an Arduino message
    #The instantaneous temperature is the first "word" in the message
    def extractTemp(self, msg):
        for i in range(len(msg)): 
            if(msg[i:i+1] == " "): 
                self.recordTemp(msg[0:i])
                return msg[0:i] 

    def getWord(self, msg, num):
        spaceCount = 0;
        start = 0;
        for i in range(len(msg)): 
            if(msg[i:i+1] == " " and start != 0):
                #self.recordHumidity(msg[firstSpace + 1: i])
                return msg[start + 1: i]
            if(msg[i:i+1] == " " and start == 0): 
                spaceCount+=1     
            if(msg[i:i+1] == " " and spaceCount == num):
                start = i            