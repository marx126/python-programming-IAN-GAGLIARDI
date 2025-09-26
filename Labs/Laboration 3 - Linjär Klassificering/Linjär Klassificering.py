# Linjär Klassificering
import urllib.request
import numpy as np
import matplotlib.pyplot as plt

data_url = "https://raw.githubusercontent.com/marx126/python-programming-IAN-GAGLIARDI/refs/heads/main/Labs/Laboration%203%20-%20Linj%C3%A4r%20Klassificering/unlabelled_data.csv"

urllib.request.urlretrieve(data_url, "unlabelled_data.csv")
data_file = "unlabelled_data.csv"

# Load data from CSV file
def load_data(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

# Define the separating line
def split_line(x, y):
    intercept = np.median(x + y)
    x_vals = np.array([np.min(x), np.max(x)])
    y_vals = -1 * x_vals + intercept
    return x_vals, y_vals, intercept

# Separate points above and below the line
def two_lits_points(x, y, intercept):
    y_line = -1 * x + intercept

    # Lists of points above and below the line
    above_list = [(x[i], y[i]) for i in range(len(x)) if y[i] > y_line[i]]
    below_list = [(x[i], y[i]) for i in range(len(x)) if y[i] < y_line[i]]

    return np.array(above_list), np.array(below_list)

# Create CSV file with points above and below the line
def create_csv(above_list, below_list):
    with open("labelled_data.csv", "w") as f:
        for point in above_list:
            f.write(f"{point[0]},{point[1]},1\n") # 1 for above the line
        for point in below_list:
            f.write(f"{point[0]},{point[1]},0\n") # 0 for below the line

# Plot data points
def plot_data(above_list, below_list, x_vals, y_vals):

    # plot poits above the line
    plt.scatter(above_list[:, 0], above_list[:, 1], s=10, color="blue", label=f"{len(above_list)} Points Above Line")

    # plot points below the line
    plt.scatter(below_list[:, 0], below_list[:, 1], s=10, color="yellow", label=f"{len(below_list)} Points Below Line")

    plt.plot(x_vals, y_vals, color="r", linewidth=2)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Data Points")
    plt.legend()
    plt.show()

def main():
    x, y = load_data(data_file)
    x_vals, y_vals, intercept = split_line(x, y)
    above_list, below_list = two_lits_points(x, y, intercept)
    plot_data(above_list, below_list, x_vals, y_vals)
    create_csv(above_list, below_list)

if __name__ == "__main__":
    main()