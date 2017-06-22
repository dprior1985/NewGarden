#Version 1.0
# 01/12/2015 - danny prior
# this script will allow for a automated temp sensor gathering and reporting


import urllib2
import RPi.GPIO as GPIO
import time
import MySQLdb
import datetime
import os
import sys

#sys.path.append('/home/pi/Desktop/GardenAutomation/modules')

import TemperatureSenor
#import lightsensor
		
		
# Open database connection
db = MySQLdb.connect("localhost","danny","danny123","NEWGARDEN" )
# prepare a cursor object using cursor() method
cursor = db.cursor()

#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)

insert ="INSERT INTO SenorLog(SensorName ,Data , DateNow )";
sql3 = "";		

def main():

	

	
	print "Temperature classmethod"
	print(datetime.datetime.now())
	temperature()
	try:
	   # Execute the SQL command
		print("commit")
   		#cursor.execute(sql3)
	   # Commit your changes in the database
		db.commit()
	except:
		print("rollback")
	   	db.rollback()

# disconnect from server
	db.close()
	
def temperature():
	

	temperature1 =	TemperatureSenor.Sensor("28-0115524404ff")
	temperature2 =	TemperatureSenor.Sensor("28-031553a54dff")
	temperature3 =	TemperatureSenor.Sensor("28-031553aaf4ff")
	temperature4 =	TemperatureSenor.Sensor("28-031553aca3ff")
	temperature5 =	TemperatureSenor.Sensor("28-031553b046ff")

	sql1 =  insert +" values('temp sensor 1','%s',now() );" % temperature1   
	sql2 =  insert +" values('temp sensor 2','%s',now() );" % temperature2  
	sql3 =  insert +" values('temp sensor 3','%s',now() );" % temperature3
	sql4 =  insert +" values('temp sensor 4','%s',now() );" % temperature4 
	sql5 =  insert +" values('temp sensor 5','%s',now() );" % temperature5  

	if ("not available" in temperature1):
		sql1 =  insert +" values('temp sensor 1','0',now() );"    
	if ("not available" in temperature2):
		sql2 =  insert +" values('temp sensor 2','0',now() );"    
	if ("not available" in temperature3):
		sql3 =  insert +" values('temp sensor 3','0',now() );"    
	if ("not available" in temperature4):
		sql4 =  insert +" values('temp sensor 4','0',now() );"    
	if ("not available" in temperature5):
		sql5 =  insert +" values('temp sensor 5','0',now() );"    
	

 
	# Execute the SQL command
	print(sql1)
  	cursor.execute(sql1)
	cursor.execute(sql2)
	cursor.execute(sql3)
	cursor.execute(sql4)
	cursor.execute(sql5)
	


if __name__ == '__main__':
	main()

