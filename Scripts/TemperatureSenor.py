
import RPi.GPIO as GPIO
import datetime
import os
import time

#GPIO PINS SETUP
GPIO.setmode(GPIO.BOARD)


def Sensor(code):
#Sensor1
	try:
		File = "/sys/bus/w1/devices/"+code+"/w1_slave"
		tempsenor = open(File)	
		temp = tempsenor.read()
		tempsenor.close()
		tempdata = temp.split("\n")[1].split(" ")[9]
		temperature = float(tempdata[2:])
		temperature = temperature / 1000
	except:
		temperature = "Sensor "+code+" not available"
		
	return  str(temperature);