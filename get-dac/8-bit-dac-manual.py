import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(leds, GPIO.OUT)
dynamic_range =3.3


def number_to_dac(value):
    bin2= [int(element) for element in bin(value)[2:].zfill(8)]
    for i in range(len(leds)):
        GPIO.output(leds[i], bin2[i])


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
