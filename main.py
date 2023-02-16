#!/bin/python3

import step
import pulse
import ramp
import exp
import sin_exp

# Exponential signals
exp.plot()
exp.stem()
exp.plot_inv()
exp.stem_inv()

# Sinusoidal signals
sin_exp.plot()
sin_exp.stem()

# Step signals
step.plot()
step.stem()

# Pulse signal
pulse.plot()

# Ramp signal
ramp.plot()
ramp.stem()
