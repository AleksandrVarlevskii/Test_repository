import signal_generator as sg
import r2r_dac as r2r
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
gpio_bits = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.3
dac = None
try:
    dac = r2r.R2R_DAC(gpio_bits, dynamic_range, True)
    start_time = time.time()

    while True :
        corrent_time = time.time() - start_time
        fx=sg.get_triange_wave_amplitude(signal_frequency, corrent_time)
        dac.set_voltage(fx*amplitude)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
