import matplotlib.pyplot as plt
import numpy as np

def plot():
    # Definir los parámetros de la señal
    t = np.linspace(0, 10, num=1000) # Tiempo
    A = 1 # Amplitud de la onda senoidal
    f = 2 # Frecuencia de la onda senoidal
    tau = 1 # Constante de tiempo de la exponencial amortiguada
    zeta = 0.5 # Coeficiente de amortiguamiento

    # Generar la señal
    y = A * np.exp(-zeta * t / tau) * np.sin(2 * np.pi * f * t)

    # Graficar la señal
    plt.plot(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal senoidal amortiguada exponencialmente')
    plt.show()

def stem():
    # Definir los parámetros de la señal
    t = np.linspace(0, 10, num=100) # Tiempo
    A = 1 # Amplitud de la onda senoidal
    f = 2 # Frecuencia de la onda senoidal
    tau = 1 # Constante de tiempo de la exponencial amortiguada
    zeta = 0.5 # Coeficiente de amortiguamiento

    # Generar la señal
    y = A * np.exp(-zeta * t / tau) * np.sin(2 * np.pi * f * t)

    # Graficar la señal
    plt.stem(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Señal senoidal amortiguada exponencialmente')
    plt.show()