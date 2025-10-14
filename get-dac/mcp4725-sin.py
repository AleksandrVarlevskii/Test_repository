import signal_generator as sg
import mcp4725_driver as mcp
import time
amplitude = 1.1
signal_frequency = 10
sampling_frequency = 1000
dac = None
try:
    dac = mcp.MCP4725(5, 0x61, True)
    start_time = time.time()

    while True :
        corrent_time = time.time() - start_time
        fx=sg.get_sin_wave_amplitude(signal_frequency, corrent_time)
        dac.set_voltage(fx*amplitude)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()