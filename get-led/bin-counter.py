import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup([9, 10], GPIO.IN)
GPIO.output(leds, 0)
num =0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    if GPIO.input(9) and num<255:
        num+=1
        print(num, dec2bin(num))
        time.sleep(0.2)
    if GPIO.input(10) and num>0:
        num-=1
        print(num, dec2bin(num))
        time.sleep(0.2)   
    for i in range(0,8) :
        GPIO.output(leds[i], dec2bin(num)[i])     