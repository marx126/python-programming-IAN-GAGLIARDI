# Klassificera Pokémons med Nearest Neighbour algoritmen
import matplotlib.pyplot as plt
import numpy as np

data_points = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Labs/Laboration 2 - Icke-Generaliserande Maskinintelligens/datapoints.txt"
test_points = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Labs/Laboration 2 - Icke-Generaliserande Maskinintelligens/testpoints.txt"

def load_data(data_path) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
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

def plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y):
    plt.scatter(pikachu_x,pikachu_y, color="yellow", label="Pikachu")
    plt.scatter(pichu_x,pichu_y, color="blue", label="Pichu")
    plt.legend()
    return plt.show()

def load_test_points(test_points):
    with open(test_points, "r") as f:
        next(f)
        points = []
        for line in f:
            if "(" in line:
                data = line.split("(")[1].split(")")[0]
                x, y = map(float, data.split(","))
                points.append([x, y])
    return np.array(points)

def euclidean_distance(p1, p2):
    pass

def main():
    pikachu_x, pikachu_y, pichu_x, pichu_y = load_data(data_points)
    plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y)


if __name__ == "__main__":
    main()