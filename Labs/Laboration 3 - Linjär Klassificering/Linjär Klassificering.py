# Linjär Klassificering
import urllib.request
import numpy as np
import matplotlib.pyplot as plt

data_url = "https://raw.githubusercontent.com/marx126/python-programming-IAN-GAGLIARDI/refs/heads/main/Labs/Laboration%203%20-%20Linj%C3%A4r%20Klassificering/unlabelled_data.csv"

urllib.request.urlretrieve(data_url, "unlabelled_data.csv")
data_file = "unlabelled_data.csv"

def load_data(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    return data

def plot_data(data):
    plt.scatter(data[:, 0], data[:, 1],s=10, c='blue', label='Data Points')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Data Points Visualization')
    plt.legend()
    plt.show()

def main():
    data = load_data(data_file)
    plot_data(data)

if __name__ == "__main__":
    main()