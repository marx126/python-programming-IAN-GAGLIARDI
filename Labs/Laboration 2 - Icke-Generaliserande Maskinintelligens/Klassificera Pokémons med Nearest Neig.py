# Klassificera Pokémons med Nearest Neighbour algoritmen
import matplotlib.pyplot as plt
import numpy as np
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Labs/Laboration 2 - Icke-Generaliserande Maskinintelligens/datapoints.txt"

pikachu_x = []
pikachu_y = []
pichu_x = []
pichu_y = []

# Read the file and append cleaned data to above pikachu and pichu data lists
with open(file_path, "r") as f: # Will change to numpy arrays in the future
    next(f)
    for line in f:
        parts = line.strip().split(",")
        width = float(parts[0])
        height = float(parts[1])
        p_type = int(parts[2])

        if p_type == 1:
            pikachu_x.append(width)
            pikachu_y.append(height)
        else:
            pichu_x.append(width)
            pichu_y.append(height)

plt.scatter(pikachu_x, pikachu_y, color="yellow", label="Pikachu")

plt.scatter(pichu_x, pichu_y, color="blue", label="Pichu")

plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.legend()
plt.show()