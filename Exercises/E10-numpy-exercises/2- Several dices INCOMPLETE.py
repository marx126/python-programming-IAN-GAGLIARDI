# Several dices
import numpy as np
import matplotlib.pyplot as plt
def sample_space():
    dice = np.arange(1, 7)
    x, y = np.meshgrid(dice, dice)
    sums = x + y
    return sums

def unique_and_counts(sums):
    unique, counts = np.unique(sums, return_counts=True)
    return unique, counts

def frequency(counts):
    total = counts.sum()
    frequencies = np.round(counts / total, 3)
    return frequencies

def plot_two_dices(unique, frequencies):    
    plt.bar(unique, frequencies)
    plt.xlabel("Unique values")
    plt.ylabel("Frequency")
    plt.title("Sum of two dices")
    return plt.show()

def main():
    sums = sample_space()
    print(f"Sample space\n{sums}")

    unique, counts = unique_and_counts(sums)
    print(f"\nUnique values\n{unique}")
    print(f"\nCounts\n{counts}")

    frequencies = frequency(counts)
    print(f"\nFrequencies\n{frequencies}")

    plot_two_dices(unique, frequencies)

if __name__ == "__main__":
    main()