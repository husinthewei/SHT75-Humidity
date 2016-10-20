import csv
class FileWriter:
    #Outputs data into a text document. Sent to a directory named "Logs" and includes a timestamp. 
    #MUST HAVE "Logs" FOLDER IN SAME DIRECTORY AS PYTHON SCRIPT
    def writeToTxt(self, Program_Start_Time, now, msg):
        with open("Logs\Log%s.txt"%(Program_Start_Time), "a") as f:        
            f.write("%s    %s\n" %(now, msg))    

    #Outputs data into a csv file. Sent to a directory named "Logs" and includes a timestamp. 
    #MUST HAVE "Logs" FOLDER IN SAME DIRECTORY AS PYTHON SCRIPT
    def writeToCsv(self, Program_Start_Time, now, msg):
        with open('Logs\Log%s.csv'%(Program_Start_Time), 'ab') as csvfile: 
            writer = csv.writer(csvfile)
 	    writer.writerow([now, str(msg)])

    def getCsvData(self, path):
        Data = [[],[]]
        with open(path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                Data[0].append(row[0])
                Data[1].append(row[1])
        return Data
