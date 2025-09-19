# Monte Carlo simulation
import numpy as np
import matplotlib.pyplot as plt
points = np.random.uniform(-1, 1, (500000, 2))
points0 = np.random.uniform(0, 0, (500000, 2))

distances = np.linalg.norm(points, axis=1)
print(distances)

inside = distances < 1
outside = distances >= 1

plt.scatter(points[inside, 0], points[inside, 1])
plt.scatter(points[outside, 0], points[outside, 1])
plt.axis("equal")
plt.legend()
plt.title("Simulation of 500000 points")
plt.show()

total_inside = np.sum(inside)
total_outside = np.sum(outside)
fraction = total_inside / (total_inside + total_outside)
print(fraction)