import numpy as np
import matplotlib.pyplot as plt

# Create a vector with n elements that go from 0 to n-1.
ram = np.arange(10)

def plot_labels(title: str):
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.show()

def plot():
    plt.plot(ram)
    plot_labels(title='Función Rampa Continua')

def stem(n: int = 10):
    plt.stem(ram)
    plot_labels(title='Función Rampa Discreta')
