import matplotlib.pyplot as plt
import numpy as np


plot_time = np.linspace(0, 5, num=1000)
stem_time = np.linspace(0, 5, num=10)
Amplitude = 1
tau = 2 # Time constant
plot_signal = Amplitude * np.exp(plot_time / tau)
stem_signal = Amplitude * np.exp(stem_time / tau)

def plot_labels(title: str):
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.show()

def plot():
    plt.plot(plot_time, plot_signal)
    plot_labels(title='Señal de crecimiento exponencial')

def stem():
    plt.stem(stem_time, stem_signal)
    plot_labels(title='Señal de crecimiento exponencial')

def plot_inv():
    plt.plot(-plot_time, plot_signal)
    plot_labels(title='Señal de crecimiento exponencial')

def stem_inv():
    plt.stem(-stem_time, stem_signal)
    plot_labels(title='Señal de crecimiento exponencial')