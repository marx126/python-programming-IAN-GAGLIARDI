# Euclidean distance
import math

def euclidean(a, b):
    return round(math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2), 1)

p1 = tuple(map(int, input("Enter first point (x, y): ").split(",")))
p2 = tuple(map(int, input("Enter second point (x, y): ").split(",")))
print(euclidean(p1, p2))

my_points = [(10, 3), (-1, -9), (10, -10), (4, -2), (9, -10)]
distances = []

for tuple in my_points:
    distances.append(euclidean((0, 0), tuple))
print(distances)