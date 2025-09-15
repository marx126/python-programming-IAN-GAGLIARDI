# Mathematical functions
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10)

def f(x):
    return x**2 - 3

def g(x):
    return 4*x - 7

y_f = f(x)
y_g = g(x)

plt.plot(x, y_f)
plt.plot(x, y_g)
plt.show()