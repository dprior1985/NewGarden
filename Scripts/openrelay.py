import RPi.GPIO as GPIO
import time
from datetime import datetime 
import os

now = datetime.now()

relay = 38




def Run(sec):

	try:
		
		if (now.minute <= 20):
			if (sec > 0):
				GPIO.setmode(GPIO.BOARD)
				GPIO.setup(relay,GPIO.OUT)
				print("Relay open")
				print(datetime.now())
				GPIO.output(relay,GPIO.LOW)
				#os.system("sudo python /home/pi/Desktop/GardenAutomation/modules/segs.py")
				time.sleep(sec)
				#sec = sec - 1


		GPIO.output(relay,GPIO.HIGH)
		print("Replay Closed")
		print(datetime.now())
	
	except:
		print ("Water pump error")
		GPIO.output(relay,GPIO.HIGH)
		
