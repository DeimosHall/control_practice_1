import matplotlib.pyplot as plt
import numpy as np

def show():
    t = np.linspace(-5, 5, num=1000)
    y = np.heaviside(t, 1)
    plt.plot(t, y)
    plt.ylim([-0.1, 1.1])
    plt.show()

def stem():
    t = np.linspace(-5, 5, num=10)
    y = np.heaviside(t, 1)
    plt.stem(t, y, use_line_collection=True)
    plt.ylim([-0.1, 1.1])
    plt.show()
