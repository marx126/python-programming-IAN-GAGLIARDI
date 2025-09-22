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
    p1 = np.asarray(p1, dtype=float)
    p2 = np.asarray(p2, dtype=float)
    return float(np.linalg.norm(p1 - p2))

def distances(test_point, pikachu_x, pikachu_y, pichu_x, pichu_y): # Returns a list of tuples (distance, pokemon_type, x, y)
    dists = []

    for i in range(len(pikachu_x)):
        dp = np.array([pikachu_x[i], pikachu_y[i]])
        d = euclidean_distance(test_point, dp)
        dists.append((d, "Pikachu", dp[0], dp[1]))

    for i in range(len(pichu_x)):
        dp = np.array([pichu_x[i], pichu_y[i]])
        d = euclidean_distance(test_point, dp)
        dists.append((d, "Pichu", dp[0], dp[1]))

    return dists

def user_input():
    while True:
        try:
            x = float(input("Enter width (cm): ").strip())
            y = float(input("Enter height (cm): ").strip())

            if x < 0 or y < 0:
                raise ValueError

            return np.array([x, y], dtype=float)
        except ValueError:
            print("Please enter valid positive numbers. Examples: 25 or 23.6")

def ten_closest(dists_list: list): # returns two lists, one with pikachu points and the other one with pichu points
    sorted_points = sorted(dists_list, key=lambda x: x[0])[:10]

    pikachu_points = []
    pichu_points = []

    for d, label, x, y in sorted_points:
        if label == "Pikachu":
            pikachu_points.append((x, y))
        else:
            pichu_points.append((x, y))

    return np.array(pikachu_points, dtype=float), np.array(pichu_points, dtype=float)

def plot_10_nearest(pikachu_points, pichu_points, user_points):
    pikachu_points = np.asarray(pikachu_points)
    pichu_points  = np.asarray(pichu_points)

    plt.scatter(pikachu_points[:, 0], pikachu_points[:, 1], label="Pikachu points", color="yellow")
    plt.scatter(pichu_points[:, 0], pichu_points[:, 1], label="Pichu points", color="blue")
    plt.scatter(user_points[0], user_points[1], label="User point", color="red")
    plt.legend()
    return plt.show()

def main():
    pikachu_x, pikachu_y, pichu_x, pichu_y = load_data(data_points)
    plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y)
    t_points = load_test_points(test_points)

    for t in t_points:
        dists = distances(t, pikachu_x, pikachu_y, pichu_x, pichu_y)
        nearest = dists[0]
        for i in dists[1:]:
            if i[0] < nearest[0]:
                nearest = i
        print(f"Sample {t} -> classified as {nearest[1]}. nearest is {nearest[1]} at distance {nearest[0]:.2f}")

    while True:
        user_test = input("Classify your own point. Type 1 to continue or 2 to skip. ")
        if user_test == "2":
            break
        elif user_test == "1":
            user_points = user_input()
            user_point_distance = distances(user_points, pikachu_x, pikachu_y, pichu_x, pichu_y)
            nearest = user_point_distance[0]
            for i in user_point_distance[1:]:
                if i[0] < nearest[0]:
                    nearest = i
            print(f"Sample {user_points} -> classified as {nearest[1]}. nearest is {nearest[1]} at distance {nearest[0]:.2f}")
            pikachu_nearest, pichu_nearest = ten_closest(distances(user_points, pikachu_x, pikachu_y, pichu_x, pichu_y))
            plot_10_nearest(pikachu_nearest, pichu_nearest, user_points)
            break
        else:
            print("Please type one of the given choices")
            


if __name__ == "__main__":
    main()