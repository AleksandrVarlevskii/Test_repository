import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
state = 0
period =1.00
while True :
    GPIO.output(26, state)
    if state == 0:
        state =2
    state -=1    
    time.sleep(period)