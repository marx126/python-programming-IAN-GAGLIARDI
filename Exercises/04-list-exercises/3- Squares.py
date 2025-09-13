# Squares
import matplotlib.pyplot as plt

squares = [x**2 for x in range(-10, 11)]

print (squares)

x = list(range(-10, 11))
y = squares

plt.plot(x, y)
plt.show()