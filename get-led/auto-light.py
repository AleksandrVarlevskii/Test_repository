import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN)
GPIO.setup(26, GPIO.OUT)
while True :
    GPIO.output(26,not (GPIO.input(6)))
    time.sleep(0.5)
    print(not (GPIO.input(6)))