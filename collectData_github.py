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

# create dictionary to figure out what season we're collecting data during
season_dict = {}
season_dict['spring'] = [3,4,5]
season_dict['summer'] = [6,7,8]
season_dict['fall'] = [9,10,11]
season_dict['winter'] = [12,1,2]

# grab keys and values
key_list = list(season_dict.keys())
val_list = list(season_dict.values())

# get today's month
season_now = datetime.now().month

# iterate through to figure out the season
ind = 0
for i in val_list:
    x = list(i)
    if season_now in x:
        position = ind
    else:
        ind += 1
season_collected = str(key_list[ind])

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
		# get time of day data collected
        time_now = datetime.now()
        currentTime = time_now.strftime("%H:%M:%S")
		# make the comma separated string
        dataLine = data + currentTime + "," + season_collected
		# parse data into csv friendly format
        dataParsed = dataLine.split(",")
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
    