import matplotlib.pyplot as plt
import numpy as np

plot_time = np.linspace(-5, 5, num=1000)
stem_time = np.linspace(-5, 5, num=10)
plot_signal = np.heaviside(plot_time, 1)
stem_signal = np.heaviside(stem_time, 1)

def plot_labels(title: str):
    plt.ylim([-0.1, 1.1])
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.show()

def plot():
    plt.plot(plot_time, plot_signal)
    plot_labels(title='Función Escalón Continua')

def stem():
    plt.stem(stem_time, stem_signal, use_line_collection=True)
    plot_labels(title='Función Escalón Discreta')
