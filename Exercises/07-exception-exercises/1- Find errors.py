# Find errors
import numpy as np

def distance(x,y):
    return np.sqrt(x**2 + y**2)

print(f"The distance between (0.5, 0.5) and origin is aroun {round(distance(0.5, 0.5), 3)}.")