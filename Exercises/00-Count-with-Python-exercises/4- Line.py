# Line
x1, y1 = 4, 4
x2, y2 = 0, 1

k = (y2 - y1) / (x2 - x1) # Slope

m = y1 - k * x1 # Constant

print (f"k = {k}, m = {m}, so the equation for the slope is y = {k}x + {int(m)}")