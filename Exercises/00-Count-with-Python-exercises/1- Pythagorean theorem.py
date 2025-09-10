# Pythagorean theorem
import math

#Solution 1 to question a)
a = 3
b = 4
hypotenuse = math.sqrt(a**2 + b**2)

print(f"The hypotenuse is {int(hypotenuse)} lenght units")

#Solution 2 to question a)
hypotenuse2 = math.hypot(a, b)

#Solution question b)
c = 7.0
d = 5.0
cathetus = math.sqrt(c**2 - d**2)

print(f"The other cathetus is {round(cathetus, 1)} length units")