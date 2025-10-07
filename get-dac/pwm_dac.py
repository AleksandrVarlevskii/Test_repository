import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.pwm_frequency = pwm_frequency

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)
        self.pwm= GPIO.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0)
        

        
    def deinit(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()
        GPIO.cleanup()


    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.pwm.ChangeDutyCycle(0)
        else:
            self.pwm.ChangeDutyCycle(voltage*100 / self.dynamic_range )
            print(f"Коэффициент  заполнения: {voltage*100 / self.dynamic_range:.2f}")

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit() 
