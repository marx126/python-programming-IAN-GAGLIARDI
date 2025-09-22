# Klassificera Pokémons med Nearest Neighbour algoritmen
import matplotlib.pyplot as plt
import numpy as np
import random

# Save files paths in variables
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
    # Basic function to plot all the data points
    plt.scatter(pikachu_x,pikachu_y, color="yellow", label="Pikachu")
    plt.scatter(pichu_x,pichu_y, color="blue", label="Pichu")
    plt.legend()
    plt.show()

def load_test_points(test_points):
    # Read and clean test points files so the data is stored as a np.array
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
    # Calculate euclidean distance, make sure arrays given are type numpy
    p1 = np.asarray(p1, dtype=float)
    p2 = np.asarray(p2, dtype=float)
    return float(np.linalg.norm(p1 - p2))

def distances(test_point, pikachu_x, pikachu_y, pichu_x, pichu_y): # Returns a list of tuples (distance, pokemon_type, x, y)
    dists = []
    # calculate distance between each test point and all data points
    # Return an organized list of tuples with all the distances
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
    # Take a point from the user. Makes sure that is valid data (No strings or negative values)
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
    # Sort list of distances by closest ones to the given point by user
    # and select the 10 first ones
    sorted_points = sorted(dists_list, key=lambda x: x[0])[:10]

    pikachu_points = []
    pichu_points = []
    
    # Separate pikachu and pichu points in different lists
    for d, label, x, y in sorted_points:
        if label == "Pikachu":
            pikachu_points.append((x, y))
        else:
            pichu_points.append((x, y))

    return np.asarray(pikachu_points, dtype=float), np.asarray(pichu_points, dtype=float)

def plot_10_nearest(pikachu_x, pikachu_y, pichu_x, pichu_y, pikachu_nearest, pichu_nearest, user_points):
    # Plot all data points
    plt.scatter(pikachu_x, pikachu_y, color="yellow", label="Pikachu")
    plt.scatter(pichu_x, pichu_y, color="blue", label="Pichu")

    # Make sure there is at least one pikachu or pichu point near point given by user
    if len(pikachu_nearest) > 0:
        plt.scatter(pikachu_nearest[:, 0], pikachu_nearest[:, 1], edgecolors='black', linewidths=2, color="yellow", label="Near pikachu")
    if len(pichu_nearest) > 0:
        plt.scatter(pichu_nearest[:, 0], pichu_nearest[:, 1], edgecolors='black', linewidths=2, color="blue", label="Near pichu")

    plt.scatter(user_points[0], user_points[1], color="red", label="Your point")

    plt.legend()
    plt.show()


def main():
    # Read data points file and plot in a graph
    pikachu_x, pikachu_y, pichu_x, pichu_y = load_data(data_points)
    plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y)

    # Read test points file and calculate distances to classify test points as
    # pikachu or pichu
    t_points = load_test_points(test_points)

    for point in t_points:
        # Calculate distance between test point and every data point
        dists = distances(point, pikachu_x, pikachu_y, pichu_x, pichu_y)
        nearest = dists[0] # helper variable, assumes the first tuple of dists list is the nearest to test point

        for i in dists[1:]:
            if i[0] < nearest[0]: # i[0] is the distance of the current tuple
                nearest = i       # nearest[0] is the distance of the current nearest

        print(f"Sample {point} -> classified as {nearest[1]}. nearest is {nearest[1]} at distance {nearest[0]:.2f}")

    # loop will run untill user gives a valid input
    while True:
        user_test = input(f"\nClassify your own point. Type 1 to continue or 2 to skip. ")

        if user_test == "2":
            break

        elif user_test == "1":
            user_point = user_input()
            # calculate distance between user point and data points
            user_point_distance = distances(user_point, pikachu_x, pikachu_y, pichu_x, pichu_y)
            nearest = user_point_distance[0] # Helper variable

            for i in user_point_distance[1:]: # Find any point closer than actual nearest
                if i[0] < nearest[0]: 
                    nearest = i

            print(f"\nClassification by nearest point:")
            print(f"Sample {user_point} -> classified as {nearest[1]}. nearest is {nearest[1]} at distance {nearest[0]:.2f}")

            # Get the 10 nearest points from the user point
            pikachu_nearest, pichu_nearest = ten_closest(distances(user_point, pikachu_x, pikachu_y, pichu_x, pichu_y))
            print("\nClassification by 10 nearest points:")

            # Classify dependig of number of pikachu/pichu near user point
            if len(pikachu_nearest) > len(pichu_nearest):
                print(f"{user_point} is classified as a Pikachu")
            elif len(pikachu_nearest) < len(pichu_nearest):
                print(f"{user_point} is classified as a Pichu")
            else:
                r_choice = random.choice(["pikachu", "Pichu"])
                print(f"Number of pichu and pikachu near your point are equal. Your point has been randomly classified as a {r_choice}")
            plot_10_nearest(pikachu_x, pikachu_y, pichu_x, pichu_y, pikachu_nearest, pichu_nearest, user_point)
            break
        else:
            print("Please type one of the given choices")

if __name__ == "__main__":
    main()