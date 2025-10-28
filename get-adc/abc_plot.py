import matplotlib.pyplot as plt



def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.xlabel('время, с', fontsize=10)
    plt.ylabel('напряжение, В', fontsize=10)
    plt.title('График зависимости напряжения на входе АЦП от времени', fontsize = 14)
    plt.grid(True)
    plt.ylim(0, max_voltage+0.05)

    plt.show()

def plot_sampling_period_hist( time_values):
    plt.figure(figsize=(10,6))
    sampling_period = []
    for i in range(1,len(time_values)):
        sampling_period.append(time_values[i]-time_values[i-1]) 
    plt.hist(sampling_period, density=False)
    plt.xlabel('период измерения, с', fontsize=10)
    plt.ylabel('количество измерений', fontsize=10)
    plt.title('Распределение периодов дискретизации измерений по времени на одно измерение', fontsize = 14)
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()


