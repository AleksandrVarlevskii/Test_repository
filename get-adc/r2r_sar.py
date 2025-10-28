import time
import r2r_adc
import abc_plot


r2r = r2r_adc.R2R_ADC(3.3)
voltage_values = []
time_values = []
start_time = time.time()
timeout = 8
if __name__ == "__main__":
    try:
        while (time.time()-start_time < timeout):
            time_values.append(time.time()-start_time)
            voltage_values.append(r2r.get_sv_voltage())

    finally:
        r2r.deinit()
        abc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.3)
        abc_plot.plot_sampling_period_hist(time_values)
        
