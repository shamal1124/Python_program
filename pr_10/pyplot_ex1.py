# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 12:14:28 2024

@author: vishv
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Demo Graph")
plt.plot(x, y,linestyle='dotted')

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()