#!/bin/python3

from square_signal import square_signal
import step
import pulse
import ramp
import exp
import sin_exp

# signal = square_signal(frequency=1, amplitude=1, duration=5)
# signal.plot()
# signal.stem(num_samples=30)

exp.plot()
exp.stem()
exp.plot_inv()
exp.stem_inv()

sin_exp.plot()
sin_exp.stem()

step.show()
step.stem()
pulse.show()
ramp.plot()
ramp.stem()