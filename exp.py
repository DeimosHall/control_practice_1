import matplotlib.pyplot as plt
import numpy as np

def plot():
    # Definir los parámetros de la señal
    t = np.linspace(0, 5, num=1000) # Tiempo
    A = 1 # Amplitud
    tau = 2 # Constante de tiempo

    # Generar la señal
    y = A * np.exp(t / tau)

    # Graficar la señal
    plt.plot(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal de crecimiento exponencial')
    plt.show()

def stem():
    # Definir los parámetros de la señal
    t = np.linspace(0, 5, num=10) # Tiempo
    A = 1 # Amplitud
    tau = 2 # Constante de tiempo

    # Generar la señal
    y = A * np.exp(t / tau)

    # Graficar la señal
    plt.stem(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal de crecimiento exponencial')
    plt.show()

def plot_inv():
    # Definir los parámetros de la señal
    t = np.linspace(0, 5, num=1000) # Tiempo
    A = 1 # Amplitud
    tau = 2 # Constante de tiempo

    # Generar la señal
    y = A * np.exp(t / tau)

    # Graficar la señal
    plt.plot(-t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal de crecimiento exponencial')
    plt.show()

def stem_inv():
    # Definir los parámetros de la señal
    t = np.linspace(0, 5, num=10) # Tiempo
    A = 1 # Amplitud
    tau = 2 # Constante de tiempo

    # Generar la señal
    y = A * np.exp(-t / tau)

    # Graficar la señal
    plt.stem(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal de crecimiento exponencial')
    plt.show()