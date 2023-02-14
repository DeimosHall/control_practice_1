import matplotlib.pyplot as plt
import numpy as np


class square_signal:
    def __init__(
        self,
        frequency: int,
        amplitude: int,
        duration: int) -> None:
        self._frequency = frequency
        self._amplitude = amplitude
        self._duration = duration


    def _create(self, num_samples: int = 1000):
        time = np.linspace(0, self._duration, num=num_samples)  
        signal = self._amplitude * np.sign(np.sin(2 * np.pi * self._frequency * time))
        return (time, signal)
    
    def plot(self):
        t, y = self._create()
        plt.plot(t, y)
        plt.show()

    def stem(self, num_samples: int = 50):
        t, y = self._create()
        plt.stem(t[::num_samples], y[::num_samples], use_line_collection=True)
        plt.show()
