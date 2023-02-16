import numpy as np
import matplotlib.pyplot as plt


def plot_labels(title: str):
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title(title)
    plt.show()

def plot(n: int = 5):
    # Create a vector with n elements with all values equal to zero.
    imp = np.zeros(n)
    # Set the value of the central sample equal to one.
    imp[n//2] = 1

    plt.stem(imp)
    plot_labels(title='Función Impulso')