# plotsquared.py
# Author: Robert O'Brien-Monk
# plot the function y = x**2

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
# get square value by multiplying each entry by itself
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()