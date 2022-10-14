import matplotlib.pyplot  as plt
import numpy as np

def find_frequency(path):
    task_file = open(path, "r")
    frequency = {1: 0}
    while True:
        line = task_file.readline()
        if not line:
            break
        if int(line) not in frequency:
            frequency[int(line)] = 1
        else:
            frequency[int(line)] += 1
    sorted_frequency = dict(sorted(frequency.items()))
    task_file.close()
    return sorted_frequency

def find_mode(frequency):
    mode = max(frequency.items(), key=lambda x: x[1])
    return mode

def find_median(frequency):
    values = list(frequency.values())
    if len(frequency) % 2 == 0:
        median = (values[int(len(frequency) / 2) - 1] + values[int(len(frequency) / 2)]) / 2
    else:
        median = values[round(len(frequency) / 2)]
    return median

def find_deviation(frequency):
    deviation = 0
    average = 0
    sumFreq = 0
    for key in frequency:
        deviation += key ** 2 * frequency[key]
        average += key * frequency[key]
        sumFreq += frequency[key]
    average /= sumFreq
    deviation /= sumFreq
    deviation -= average ** 2
    return deviation

def print_frequency(frequency):
    comb_freq = 0
    print("Item | Freq | Comb freq")
    for key in frequency:
        comb_freq += frequency[key]
        print(key, " | ", frequency[key], " | ", comb_freq)

def task():
    frequency = find_frequency("task_01_data/input_10.txt")
    print("Mode: ", find_mode(frequency))
    print("Median: ", find_median(frequency))
    deviation = find_deviation(frequency)
    print("Deviation: ", deviation)
    print("Mean square deviation of the distribution: ", deviation ** (0.5))

    print_frequency(frequency)
    plt.bar(frequency.keys(), frequency.values(), 1, color='g')
    plt.grid()
    plt.show()

task()




