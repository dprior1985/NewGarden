import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

now = datetime.now()

GPIO.setmode(GPIO.BOARD)
relay = 38
GPIO.setup(relay,GPIO.OUT)



try:
        GPIO.output(relay,GPIO.LOW)
        time.sleep(1)
        GPIO.output(relay,GPIO.HIGH)
        print("Replay Closed")
        print(datetime.now())

except:
        print ("Water pump error")
        GPIO.output(relay,GPIO.HIGH)

