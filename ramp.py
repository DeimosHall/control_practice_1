import numpy as np
import matplotlib.pyplot as plt

def plot(n: int = 10):
    # Crea un vector con n elementos que van desde 0 hasta n-1.
    ram = np.arange(n)

    # Ejemplo de uso
    n = 10
    plt.plot(ram)
    plt.title('Función Rampa')
    plt.xlabel('n')
    plt.ylabel('Amplitud')
    plt.show()

def stem(n: int = 10):
    # Crea un vector con n elementos que van desde 0 hasta n-1.
    ram = np.arange(n)

    # Ejemplo de uso
    n = 10
    plt.stem(ram)
    plt.title('Función Rampa')
    plt.xlabel('n')
    plt.ylabel('Amplitud')
    plt.show()
