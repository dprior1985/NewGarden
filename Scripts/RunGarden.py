#Version 1.0
# 31/08/2015 - danny prior
# this script will allow for a automated garden water system which uses senors to determine what needs to be watered


import urllib2
import json
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime
import os
import sys
from decimal import Decimal

import openrelay
		
		
# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","NEWGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
Water = 0;

#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)

def main():

	global SleepTime;
	
	Water=decide()
		
	if (Water >= 1):
		print "openrelay classmethod"
		print(datetime.datetime.now())
		if (Water >= 1):
			if (Water == 1):
				SleepTime = 120 #summer times
			#	SleepTime = 20 #winter times
			if (Water == 2):
				SleepTime = 120 #summer times
			#	SleepTime = 20 #winter times
			if (Water == 3):
				SleepTime = 60 #summer times
			#	SleepTime = 10 #winter times
			if (Water == 4):
				SleepTime = 120 #summer times
			#	SleepTime = 20 #winter times
			if (Water == 5):
				SleepTime = 150 #summer times
			#	SleepTime = 30 #winter times
			if (Water == 6):
				SleepTime = 160 #summer times
			#	SleepTime = 30 #winter times			
			if (Water == 7):
				SleepTime = 300 #summer times
			#	SleepTime = 20 #winter times
			
			os.system("python /home/pi/SillyTweeter/SillyTweeter.py 'Message' 'The Garden Is Started to be Watered'")			
			openrelay.Run(SleepTime)
			os.system("python /home/pi/SillyTweeter/SillyTweeter.py 'Message' 'The Garden Is Finished Being Watered'")
			#sleep(SleepTime)
			#openrelay.Run(2)


	if (Water <= 0):
		print('Not Active')
		print(datetime.datetime.now())


	print "END"
	print(datetime.datetime.now())
	#RunNumberClean()
# disconnect from server
	db.close()

	
def decide():

	waterlogic = -10;
	TimeToWater = -1;

	
	try:
		cursor.execute("select 1 as Note from Schedule where  minute(now()) <= 15 and hour(now()) in ( select Time from Schedule ) limit 1;")
	        for row in cursor.fetchall():
       		        TimeToWater = (row[0])

		

	except Exception ,e:
		print "failure with schedule run : "+ str(e)
	   	db.rollback()		

	if (TimeToWater <= -1):
		waterlogic = -10;		


	if (TimeToWater >= 1): 		


		x=Decimal(5)
		
		x1=[]
		cursor.execute("select MAX(cast(Data as decimal(16,2))) from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '24:00:00') <= DateNow ; " )
			for row in cursor.fetchall():
				x = (row[0])
		
		
		waterlogic = 1;
		if (x < 5):
			waterlogic = -1;				
		
		if (x >= 5 and x < 12):
			waterlogic = 3;				

		if (x >= 12 and x <  16):
			waterlogic = 4;				
		
		
		if (x >= 16 and x <  20):
			waterlogic = 5;				
		
		if (x >= 20 and x <  25):
			waterlogic = 6;				
		
		if (x >= 25):
			waterlogic = 7;				
	
	return waterlogic

if __name__ == '__main__':
	main()


