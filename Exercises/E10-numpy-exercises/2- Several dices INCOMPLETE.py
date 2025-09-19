# Several dices
import numpy as np
import matplotlib.pyplot as plt

dice = np.arange(1, 7)

x, y = np.meshgrid(dice, dice)
sums = x + y
print(f"Sample space\n{sums}")


unique, counts = np.unique(sums, return_counts=True)
print(f"\nUnique values\n{unique}")
print(f"\nCounts\n{counts}")

total = counts.sum()
frequencies = np.round(counts / total, 3)
print(f"\nFrequencies\n{frequencies}")

plt.bar(unique, frequencies)
plt.xlabel("Unique values")
plt.ylabel("Frequency")
plt.title("Sum of two dices")
plt.show()