import time
import numpy as np


def get_sin_wave_amplitude(fred, time):
    return (np.sin(2 * np.pi * fred * time)+1)/2


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1.0/sampling_frequency)


def get_triange_wave_amplitude(fred, time):
    period = 1.0/fred
    position = (time % period)/ period
    if position < 0.5:
        return 2*position
    else:
        return 2*(1-position)
