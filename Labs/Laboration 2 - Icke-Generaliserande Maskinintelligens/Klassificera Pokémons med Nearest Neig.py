# Klassificera Pokémons med Nearest Neighbour algoritmen
import matplotlib.pyplot as plt
import numpy as np
data_points = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Labs/Laboration 2 - Icke-Generaliserande Maskinintelligens/datapoints.txt"
test_points = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Labs/Laboration 2 - Icke-Generaliserande Maskinintelligens/testpoints.txt"

def load_data(data_path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Read file and create a numpy array
    data = np.loadtxt(data_path, delimiter=",", skiprows=1)
    # Separate width, height and pokemon type
    x = data[:, 0]
    y = data[:, 1]
    p_type = data[:, 2]
    # Boolean array indexing to order x and y by type of pokemon
    pikachu_x = x[p_type == 1]
    pikachu_y = y[p_type == 1]
    pichu_x = x[p_type == 0]
    pichu_y = y[p_type == 0]
    return pikachu_x, pikachu_y, pichu_x, pichu_y

def plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y) -> plt.show:
    plt.scatter(pikachu_x,pikachu_y, color="yellow", label="Pikachu")
    plt.scatter(pichu_x,pichu_y, color="blue", label="Pichu")
    plt.legend()
    return plt.show()

def main():
    pikachu_x, pikachu_y, pichu_x, pichu_y = load_data(data_points)
    plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y)

main()