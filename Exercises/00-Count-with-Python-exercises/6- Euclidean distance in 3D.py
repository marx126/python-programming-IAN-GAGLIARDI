# Euclidean distance in 3D
import math

p1, p2, p3 = 2,1,4
q1, q2, q3 = 3,1,0

distance = math.sqrt((p1 - q1)**2 + (p2 - q2)**2 + (p3 - q3)**2)

print(f"The distance is around {round(distance, 2)} length units.")