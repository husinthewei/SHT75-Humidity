SHT75 Sensor Project

How to run main.py (NOTE: CURRENTLY ON WORKS ON WINDOWS):
  Requirements-
	*python:
	  There are many options to install python. There are tutorials for Windows if googled, or you could download Enthought Canopy.
	*pip:
	  Download http://www.pip-installer.org/en/latest/installing.html
	  In cmd, cd to the directory of the file downloaded and type: python get-pip.py
	*pyserial:
	  After pip is installed, type in cmd: python -m pip install pyserial
	*pyqtgraph
	  After pip is installed, type in cmd: python -m pip install pyqtgraph
	*matplotlib
	  After pip is installed, type in cmd: python -m pip install matplotlib
  Procedure-
	1. cd to the directory of the python script. Ex: cd C:\Users\Your_Username\Documents\Github\SHT75-Humidity\Python
	2. type: python -B main.py
	3. Enter the com port. Ex: Usually type: 0 
	4. Enter how often you want data output

How to run SHT75:
  Requirements-
	*Arduino IDE:
	  https://www.arduino.cc/en/Main/Software
  Procedure-
	1. The Arduino program is likely already on the board. It automatically starts running when the Arduino is turned on.
	2. If not loaded on, run the Arduino IDE and open SHT75
	3. Click the upload button on the top left

Where to find data outputs: 
	- The data outputs are in a folder called "Logs" inside the PythonScripts directory
	- They are in the form of csv files and include a timestamp in their names. 