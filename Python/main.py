import Grapher
import time
Plotter = Grapher.Grapher(1) 

Plotter.plotData(1,1)

for i in range(100): 
    Plotter.plotData(i, i)
    time.sleep(1)
