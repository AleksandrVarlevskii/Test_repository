import signal_generator as sg
import pwm_dac as pwm
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
dac = None
try:
    dac = pwm.PWM_DAC(12, 500, 3.290, True)
    start_time = time.time()

    while True :
        corrent_time = time.time() - start_time
        fx=sg.get_triange_wave_amplitude(signal_frequency, corrent_time)
        dac.set_voltage(fx*amplitude)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
