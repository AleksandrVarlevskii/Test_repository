import time
import mcp3021_driver
import abc_plot

pwr = mcp3021_driver.MCP3021(5)
voltage_values = []
time_values = []
start_time = time.time()
timeout = 15
if __name__ == "__main__":
    try:
        while (time.time()-start_time < timeout):
            time_values.append(time.time()-start_time)
            voltage_values.append(pwr.get_voltage())

    finally:
        pwr.deinit()
        abc_plot.plot_voltage_vs_time(time_values, voltage_values, 5)
        abc_plot.plot_sampling_period_hist(time_values)
        
