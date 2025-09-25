# Klassificera Pokémons med Nearest Neighbour algoritmen
import matplotlib.pyplot as plt
import numpy as np
import random
import urllib.request
# Save files paths in variables
data_url = "https://raw.githubusercontent.com/marx126/python-programming-IAN-GAGLIARDI/refs/heads/main/Labs/Laboration%202%20-%20Icke-Generaliserande%20Maskinintelligens/datapoints.txt"
test_url = "https://raw.githubusercontent.com/marx126/python-programming-IAN-GAGLIARDI/refs/heads/main/Labs/Laboration%202%20-%20Icke-Generaliserande%20Maskinintelligens/testpoints.txt"

try:
    urllib.request.urlretrieve(data_url, "datapoints.txt")
except Exception as e:
    print(f"Fail to download datapoints.txt: {e}")

try:
    urllib.request.urlretrieve(test_url, "testpoints.txt")
except Exception as e:
    print(f"Fail to download testpoints.txt: {e}")

data_points = "datapoints.txt"
test_points = "testpoints.txt"

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
    distances_list = []
    # calculate distance between each test point and all data points
    for i in range(len(pikachu_x)):
        dp = np.array([pikachu_x[i], pikachu_y[i]])
        d = euclidean_distance(test_point, dp)
        distances_list.append((d, "Pikachu", dp[0], dp[1]))

    for i in range(len(pichu_x)):
        dp = np.array([pichu_x[i], pichu_y[i]])
        d = euclidean_distance(test_point, dp)
        distances_list.append((d, "Pichu", dp[0], dp[1]))
    # Return an organized list of tuples with all the distances
    return distances_list

def classify_point(point, pikachu_x, pikachu_y, pichu_x, pichu_y):
    # Classify a single point by finding the nearest neighbour
    dists = distances(point, pikachu_x, pikachu_y, pichu_x, pichu_y)
    nearest = min(dists, key=lambda x: x[0])  # Find the nearest neighbour
    print(f"Sample {point} -> classified as {nearest[1]}. Nearest point is a {nearest[1]} at distance {nearest[0]:.2f}")
    return nearest

def classify_test_file_points(test_points, pikachu_x, pikachu_y, pichu_x, pichu_y):
    # Read test points file and calculate distances to classify test points as
    # pikachu or pichu
    t_points = load_test_points(test_points)

    for point in t_points:
        classify_point(point, pikachu_x, pikachu_y, pichu_x, pichu_y)

def user_point_classification(pikachu_x, pikachu_y, pichu_x, pichu_y):
    while True:
        user_test = input(f"\nClassify your own point. Type 1 to continue or 2 to skip. ")

        if user_test == "2":
            return

        elif user_test == "1":
            user_point = user_input()

            # Classify point given by user
            nearest = classify_point(user_point, pikachu_x, pikachu_y, pichu_x, pichu_y)

            # Get the 10 nearest points from the user point
            pikachu_nearest, pichu_nearest = ten_closest(distances(user_point, pikachu_x, pikachu_y, pichu_x, pichu_y))
            print("\nClassification by 10 nearest points:")

            # Classify dependig of number of pikachu/pichu near user point
            if len(pikachu_nearest) > len(pichu_nearest):
                print(f"Sample {user_point} -> is classified as a Pikachu. Number of pikachus nearby: {len(pikachu_nearest)}\n")
            elif len(pikachu_nearest) < len(pichu_nearest):
                print(f"Sample {user_point} -> is classified as a Pichu. Number of pichus nearby: {len(pichu_nearest)}\n")
            else:
                print(f"Number of pichu and pikachu near {user_point} are equal. {user_point} has been classified as {nearest[1]} by nearest point instead.\n")
            plot_10_nearest(pikachu_x, pikachu_y, pichu_x, pichu_y, pikachu_nearest, pichu_nearest, user_point)
            return
        else:
            print("Please type one of the given choices")

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
        plt.scatter(pikachu_nearest[:, 0], pikachu_nearest[:, 1], edgecolors="black", linewidths=2, color="yellow", label="Near pikachu")
    if len(pichu_nearest) > 0:
        plt.scatter(pichu_nearest[:, 0], pichu_nearest[:, 1], edgecolors="black", linewidths=2, color="blue", label="Near pichu")

    plt.scatter(user_points[0], user_points[1], color="red", label="Your point")

    plt.legend()
    plt.show()

def split_data(pikachu_x, pikachu_y, pichu_x, pichu_y, seed=None):

    if seed is not None:
        random.seed(seed)

    # zip together x and y so its easier to work with the data
    pikachu_points = list(zip(pikachu_x, pikachu_y))
    pichu_points = list(zip(pichu_x, pichu_y))

    random.shuffle(pikachu_points)
    random.shuffle(pichu_points)
    
    # split data in 50 training points and 25 test points
    pikachu_train_data = pikachu_points[:50]
    pikachu_test_data = pikachu_points[50:75]

    pichu_train_data = pichu_points[:50]
    pichu_test_data = pichu_points[50:75]
    
    # unzip to have different arrays with all x and y values
    pikachu_x_train, pikachu_y_train = zip(*pikachu_train_data)
    pikachu_x_test, pikachu_y_test = zip(*pikachu_test_data)

    pichu_x_train, pichu_y_train = zip(*pichu_train_data)
    pichu_x_test, pichu_y_test = zip(*pichu_test_data)

    return (
        np.asarray(pikachu_x_train, dtype=float),
        np.asarray(pikachu_y_train, dtype=float),
        np.asarray(pikachu_x_test,  dtype=float),
        np.asarray(pikachu_y_test,  dtype=float),
        np.asarray(pichu_x_train,   dtype=float),
        np.asarray(pichu_y_train,   dtype=float),
        np.asarray(pichu_x_test,    dtype=float),
        np.asarray(pichu_y_test,    dtype=float))

def predict_10nn_points(x, y,
                        pikachu_x_train, pikachu_y_train, 
                        pichu_x_train, pichu_y_train,):
    
    # Combine training data into a single array
    x_train = np.column_stack([
    np.r_[pikachu_x_train, pichu_x_train],
    np.r_[pikachu_y_train, pichu_y_train]])

    # Create labels for training data: 1 for Pikachu, 0 for Pichu
    y_train = np.r_[np.ones(len(pikachu_x_train),dtype=int),
                np.zeros(len(pichu_x_train), dtype=int)]
    
    # Calculate distances from the point (x, y) to all training points
    test_points = np.array([x, y])
    distances = np.linalg.norm(x_train - test_points, axis=1)

    # Sort distances and get indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:10]
    nearest_labels = y_train[nearest_indices]

    # Count occurrences of each class in the nearest neighbors
    pikachu_count = np.sum(nearest_labels == 1)
    pichu_count = np.sum(nearest_labels == 0)

    # Determine the predicted class based on counts
    if pikachu_count > pichu_count:
        return "Pikachu"
    elif pichu_count > pikachu_count:
        return "Pichu"
    else:
        # Tie-breaking strategy
        if pikachu_count == pichu_count:
            return "Pikachu" if nearest_labels[0] == 1 else "Pichu"
        
def calculate_accuracy(predictions, true_labels):

    # Calculate accuracy given a list of predictions and true labels
    tp = sum(1 for pred, true in zip(predictions, true_labels) if pred == "Pikachu" and true == "Pikachu")
    tn = sum(1 for pred, true in zip(predictions, true_labels) if pred == "Pichu" and true == "Pichu")
    total = len(true_labels)
    return (tp + tn) / total

def accuracy_over_iterations(pikachu_x, pikachu_y, pichu_x, pichu_y):
    accuracies = []
    for i in range(10):
        print(f"Iteration {i + 1}:")
        pikachu_x_train, pikachu_y_train, pikachu_x_test, pikachu_y_test, \
        pichu_x_train, pichu_y_train, pichu_x_test, pichu_y_test = split_data(pikachu_x, pikachu_y, pichu_x, pichu_y, seed=i)

        # Lists to store predictions and true labels
        predictions = []
        true_labels = []

        # Classify test points of Pikachu
        for x, y in zip(pikachu_x_test, pikachu_y_test):
            pred = predict_10nn_points(x, y, pikachu_x_train, pikachu_y_train, pichu_x_train, pichu_y_train)
            predictions.append(pred)
            true_labels.append("Pikachu")

        # Classify test points of Pichu
        for x, y in zip(pichu_x_test, pichu_y_test):
            pred = predict_10nn_points(x, y, pikachu_x_train, pikachu_y_train, pichu_x_train, pichu_y_train)
            predictions.append(pred)
            true_labels.append("Pichu")

        # Calculate accuracy
        accuracy = calculate_accuracy(predictions, true_labels)
        accuracies.append(accuracy)
        print(f"Accuracy for iteration {i + 1}: {accuracy:.2f}")
    return accuracies

# Calculate and print mean accuracy
def calculate_mean_accuracy(accuracies):
    mean_accuracy = sum(accuracies) / len(accuracies)
    print(f"\nMean accuracy over 10 iterations: {mean_accuracy:.2f}")
    return mean_accuracy

# Plot accuracy over 10 iterations
def plot_accuracy(accuracies, mean_accuracy):
    plt.plot(range(1, 10 + 1), accuracies, marker="o", label="Accuracy per iteration")
    plt.axhline(y=mean_accuracy, color="r", linestyle="--", label=f"Mean accuracy: {mean_accuracy:.2f}")
    plt.title("Accuracy over iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.show()

# Main function, I have tried to keep it as clean and simple as possible
def main():
    # Read data points file and plot in a graph
    pikachu_x, pikachu_y, pichu_x, pichu_y = load_data(data_points)
    plot_data_points(pikachu_x, pikachu_y, pichu_x, pichu_y)

    # Classify test points from file and print results
    classify_test_file_points(test_points, pikachu_x, pikachu_y, pichu_x, pichu_y)

    # Classify user point by nearest neighbour and 10 nearest neighbours
    user_point_classification(pikachu_x, pikachu_y, pichu_x, pichu_y)

    # Calculate and print accuracy over 10 iterations
    accuracies = accuracy_over_iterations(pikachu_x, pikachu_y, pichu_x, pichu_y)

    # Calculate and print mean accuracy
    mean_accuracy = calculate_mean_accuracy(accuracies)

    # Plot accuracies over iterations
    plot_accuracy(accuracies, mean_accuracy)

if __name__ == "__main__":
    main()