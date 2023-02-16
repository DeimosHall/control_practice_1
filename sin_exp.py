import matplotlib.pyplot as plt
import numpy as np


plot_time = np.linspace(0, 10, num=1000)
stem_time = np.linspace(0, 10, num=100)
amplitude = 1
frequency = 2
tau = 1 # Time constant of the exponential damping
zeta = 0.5 # Damping coefficient

plot_signal = amplitude * np.exp(-zeta * plot_time / tau) * np.sin(2 * np.pi * frequency * plot_time)
stem_signal = amplitude * np.exp(-zeta * stem_time / tau) * np.sin(2 * np.pi * frequency * stem_time)

def plot_labels(title: str):
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.show()

def plot():
    plt.plot(plot_time, plot_signal)
    plot_labels(title='Señal senoidal amortiguada exponencialmente continua')

def stem():
    plt.stem(stem_time, stem_signal)
    plot_labels(title='Señal senoidal amortiguada exponencialmente discreta')