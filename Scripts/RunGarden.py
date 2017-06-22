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
Weather1 ="";
RunNumber = 0;
Water = 0;
cnt = 0;
icon_url = "";

#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)

insert ="INSERT INTO ControlLog(LogDescription,ActionName,SaveData,ControlId,DateNow)";
sql3 = "";		

def main():

		
	global Water;
	global SleepTime;

	decide()
	
	
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
				SleepTime = 120 #summer times
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

	global Water;


	waterlogic = -10;
	TimeToWater = -1;

	#if schedule run
#	sq53 =  "update RunNumber set Water = 10 where RunnumberId = %s and hour(now()) in ( select Time from Schedule );" %  (int(RunNumber))
	
	try:
	   # Execute the SQL command
 #  		cursor.execute(sq53)
	   # Commit your changes in the database
#		db.commit()
		cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;select 1 as Note from Schedule where  minute(now()) <= 15 and hour(now()) in ( select Time from Schedule ) limit 1;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
	        for row in cursor.fetchall():
       		        TimeToWater = (row[0])

		

	except Exception ,e:
		print "failure with schedule run : "+ str(e)
	   	db.rollback()		

        if (TimeToWater <= -1):

                try:
                   # Execute the SQL command
                        cursor.execute(sq53)
                   # Commit your changes in the database
                        db.commit()
                        waterlogic = -10;
                except Exception ,e:
                        print "not to schdule : "+ str(e)
                        db.rollback()
		
		

	if (TimeToWater >= 1): 		


		x=Decimal(5)
		
		x1=[]
		cursor.execute("select MAX(cast(Data as decimal(16,2))) from SenorLog where SensorName = 'temp sensor 2' and subtime(now(), '24:00:00') <= DateNow ; " )
		for row in cursor.fetchall():

		x = (row[1])
		x1.append(x)


		
		
		
		
		
		
		

	#Default to water
#		sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;update RunNumber set Water = 1 where  RunnumberId in (select RunNumberId from ControlLog where RunNumberId = %s );SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %  (int(RunNumber))
		
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = 1;
		except Exception ,e:
			print "failure default to water : "+ str(e)
			db.rollback()

	#if temp < 5 then dont water
		#sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;update RunNumber set Water = -1 where Water >= 0 and  RunnumberId in ( select RunNumberId from ControlLog where cast(SaveData as decimal(16,2)) < 5 and ActionName = 'temp sensor 2' and LogDescription = 'Temp C' ) and RunNumberId = %s;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;" 
		
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = -1;
		except Exception ,e:
			print "failure with temp <12 "
			db.rollback()






	#if temp >= 5 < 12 then water
#		sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;update RunNumber set Water = 4 where Water <= 1 and  RunnumberId in ( select RunNumberId from ControlLog where cast(SaveData as decimal(16,2)) >=5 and cast(SaveData as decimal(16,2)) < 12 and Active = 1 and ActionName = 'temp sensor 2' and LogDescription = 'Temp C' ) and RunNumberId = %s ;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %  (int(RunNumber))
		
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = 3;
		except Exception ,e:
			print "failure with temp >=12 < 16 then water  : "+ str(e)
			db.rollback()


			
			
	#if temp >= 12 < 16 then water
#		sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;update RunNumber set Water = 4 where Water <= 1 and  RunnumberId in (select RunNumberId from ControlLog where cast(SaveData as decimal(16,2)) >=12 and cast(SaveData as decimal(16,2)) < 16  and Active = 1 and ActionName = 'temp sensor 2' and LogDescription = 'Temp C' ) and RunNumberId = %s ;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %  (int(RunNumber))
		
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = 4;
		except Exception ,e:
			print "failure with temp >=12 < 16 then water  : "+ str(e)
			db.rollback()



	#if temp >= 16  < 20 then water
#		sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;update RunNumber set Water = 5 where Water <= 1 and  RunnumberId in (select RunNumberId from ControlLog where cast(SaveData as decimal(16,2)) >=16 and cast(SaveData as decimal(16,2)) < 20 and Active = 1 and ActionName = 'temp sensor 2' and LogDescription = 'Temp C' ) and RunNumberId = %s ;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %  (int(RunNumber))
		
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = 5;
		except Exception ,e:
			print "failure with temp >16  < 20 then water  : "+ str(e)
			db.rollback()



			
	#if temp >= 20  then water
#		sq53 =  "SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;	update RunNumber set Water = 6 where Water <= 1 and  RunnumberId in (select RunNumberId from ControlLog where cast(SaveData as decimal(16,2)) >=20 and Active = 1 and ActionName = 'temp sensor 2' and LogDescription = 'Temp C' ) and RunNumberId = %s ;  (int(RunNumber));SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %
		try:
		   # Execute the SQL command
			cursor.execute(sq53)
		   # Commit your changes in the database
			db.commit()
			waterlogic = 6;
		except Exception ,e:



			print "failure with temp >= 20  then water  : "+ str(e)
			db.rollback()

	

		cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;select Water from RunNumber where RunNumberId = %s ;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;" %  (int(RunNumber)))
		for row in cursor.fetchall():

			Water = (row[0])



def RunNumber():

	sql =  "insert into RunNumber(DateNow,Water)  values(now(),0);"
	
	db.commit()
		
	global RunNumber;
	global sql3;

	cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;select RunNumberID from RunNumber ORDER BY RunNumberId DESC limit 1;SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;")
	for row in cursor.fetchall():

		RunNumber = (row[0])
	
	sql3 =  "update ControlLog set RunNumberId = %s ,Active = 1 where RunNumberId is null ;" %  (int(RunNumber))
	
	

	


if __name__ == '__main__':
	main()

 	GPIO.cleanup()
