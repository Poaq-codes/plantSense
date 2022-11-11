#%%
# import modules
# --------------
import serial
import csv
from datetime import date
import time

#%%
# setup
# --------------
# grab the port
arduino = serial.Serial('COM3', 9600, timeout=.1)

# create file name
date = date.today()
fileName = "path/to/dir" + str(date) + ".csv"

#%%
# main data collector
# --------------
# loop to hold desired number of data points
sensorData = []
# 12 hours x q5min = 144
samples = 144
line = 1
while line <= samples:
    getData = arduino.readline()
    dataString = getData.decode('utf-8')
	# removes newline character
    data = dataString[:-2]
    # make sure the data isn't just a blank line
    if data:
        dataParsed = data.split(",")
        sensorData.append(dataParsed)
        line += 1
		# wait for arduino to measure again
        time.sleep(300)

# write collected data to file		
with open(fileName, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sensorData)

# close port    
arduino.close()
    