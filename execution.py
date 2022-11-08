from interpolationSplines import interpolationSplines
import matplotlib.pyplot as plt
import numpy as np
from numpy import nbytes, zeros,array,dot,linspace, linalg

nb = 300

## Courbe 1 ##
x1 = array([0.9, 1.3, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5, 6, 7, 8, 9.2, 10.5, 11.3, 11.6, 12, 12.6, 13, 13.3])
y1 = array([1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.24])

[X1, Y1] = interpolationSplines(x1, y1, nb)


## tracer ##
plt.plot(X1, Y1)
plt.title("Mon Canard Numérique")
plt.show()