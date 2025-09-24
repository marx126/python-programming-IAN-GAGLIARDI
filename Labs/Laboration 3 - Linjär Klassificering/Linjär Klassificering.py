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

# Calculate mean of points
def calculate_mean(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    return mean_x, mean_y

# Calculate slope
def calculate_slope(x, y, mean_x, mean_y):
    slope = np.sum((x - mean_x) * (y - mean_y)) / np.sum((x - mean_x) ** 2)
    return slope

# Calculate intercept
def calculate_intercept(mean_x, mean_y, slope):
    intercept = mean_y - slope * mean_x
    return intercept

# Plot points and best fit line
def plot_best_fit_line(x, y, slope, intercept):
    plt.scatter(x, y, s=10, c='blue', label='Data Points')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Best Fit Line Visualization')
    
    # Define the range for the best fit line using the minimum and maximum values of x
    x_fit = np.array([np.min(x), np.max(x)])

    # y = kx + m
    y_fit = slope * x_fit + intercept
    plt.plot(x_fit, y_fit, color='red', label='Best Fit Line')

    plt.legend()
    plt.show()

def main():
    x, y = load_data(data_file)

    mean_x, mean_y = calculate_mean(x, y)
    print(f"Mean of Feature 1: {mean_x}, Mean of Feature 2: {mean_y}")

    slope = calculate_slope(x, y, mean_x, mean_y)
    print(f"Slope of the best fit line: {slope}")

    intercept = calculate_intercept(mean_x, mean_y, slope)
    print(f"Intercept of the best fit line: {intercept}")
    
    plot_best_fit_line(x, y, slope, intercept)

if __name__ == "__main__":
    main()