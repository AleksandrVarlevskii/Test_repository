import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
GPIO.setup(bits_gpio, GPIO.OUT, initial = 0)
GPIO.output(bits_gpio, 0)
