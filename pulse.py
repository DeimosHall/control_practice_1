import numpy as np
import matplotlib.pyplot as plt

def show(n: int = 5):
    # Crea un vector con n elementos con todos los valores igual a cero.
    imp = np.zeros(n)
    # Establece el valor de la muestra central igual a uno.
    imp[n//2] = 1

    # Ejemplo de uso
    n = 20
    plt.stem(imp)
    plt.title('Función Impulso')
    plt.xlabel('n')
    plt.ylabel('Amplitud')
    plt.show()