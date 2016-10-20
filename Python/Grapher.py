import collections
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import time
import pyqtgraph as pg
import matplotlib.pyplot as plt
import FileWriter
import datetime
from matplotlib.backends.backend_pdf import PdfPages

class Grapher:
    #Displays the past 8640 samples.
    #8640 samples represents 24 hours of data taken every 10 seconds
    #Once the deque's are filled, they start replacing the oldest elements
    #Therefore, runs for more than 24 hours and only shows last 24 hours.
    def __init__(self, ProgramStartTime = time.strftime("%Y%m%dT%H%M%S")):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        self.xData = collections.deque(maxlen=8640) 
        self.yData = collections.deque(maxlen=8640) 
        self.Program_Start_Time = ProgramStartTime  
        self.app = QtGui.QApplication([])
        self.p = pg.plot()
        self.curve = self.p.plot(pen=pg.mkPen('r', width=3))      
        self.initializeGraph() 

        
    #Setting how the plot looks
    def initializeGraph(self):
        self.p.setRange(yRange=[-20,32])
        self.p.setTitle('Temp vs. Time')
        self.p.setLabel(axis = 'left', text = 'Temperature (C)')
        self.p.setLabel(axis = 'bottom', text = "Hours since %s"%self.Program_Start_Time) 
        self.p.showGrid(x=True, y=True, alpha=None)

    def plotData(self,x,y):
        self.xData.append(x) 
        self.yData.append(y)
        self.curve.setData(list(self.xData),list(self.yData)) #Plotting the data   
    
    def processEvents(self):
        self.app.processEvents()
                
    #Produce a "good looking" graph with matplotlib
    #Also, export it to a PDF file
    #Creates using the CSV file
    def produceGraph(self, path):
        File_Writer = FileWriter.FileWriter()
        data = File_Writer.getCsvData(path)
        startTime = data[0][0]
        plt.figure()
        plt.clf()
        plt.ylim(-20, 30)
        xData = self.extractTimeElapsed(data[0], startTime)
        plt.plot(xData,data[1]) 
        plt.ylabel('Temp(C)')
        plt.xlabel('Hours since %s'%startTime)
        plt.title('Temp vs. Time')
        fname = self.extractFileName(path)
        pp = PdfPages('Graphs\%s.pdf'%fname)
        pp.savefig()
        pp.close()
    
    #Extract the file name from the path
    def extractFileName(self, path): 
        fname = path.split('\\')[-1]
        fname = fname.split('.')[0]
        return fname
        
    def extractTimeElapsed(self, data, t0):
        t0 = datetime.datetime.strptime(t0,"%Y-%m-%dT%H:%M:%S")         
        for i in range(len(data)):
            t = datetime.datetime.strptime(data[i],"%Y-%m-%dT%H:%M:%S")  
            t = ((t-t0).total_seconds())/3600 #hours elapsed 
            data[i] = t
        return data      