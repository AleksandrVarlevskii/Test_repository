import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, value):
        bin2= [int(element) for element in bin(value)[2:].zfill(8)]
        for i in range(len(self.gpio_bits)):
            GPIO.output(self.gpio_bits[i], bin2[i] )

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            self.set_number(0)
        else:
            self.set_number(int(voltage / self.dynamic_range * 255))



if __name__ == "__main__":
    try:
        # Если сделать dynamic_range равным 3.3 результаты будут как и в 8-bit-dac-manual
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()