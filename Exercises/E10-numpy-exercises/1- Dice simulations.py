# Dice simulations
import matplotlib.pyplot as plt
import numpy as np

def dice_mean():
    dice_faces = np.arange(1,7)
    return dice_faces.mean()

def dice_rolls():
    rolls_10 = np.random.randint(1,7,10)
    rolls_100 = np.random.randint(1,7,100)
    rolls_1000 = np.random.randint(1,7,1000)
    rolls_10000 = np.random.randint(1,7,10000)
    rolls_100000 = np.random.randint(1,7,100000)
    rolls_1000000 = np.random.randint(1,7,1000000)
    rolls_10000000 = np.random.randint(1,7,10000000)
    return rolls_10.mean(), rolls_100.mean(), rolls_1000.mean(), rolls_10000.mean(), rolls_100000.mean(), rolls_1000000.mean(), rolls_10000000.mean()

def rolls_mean(y1, y2, y3, y4, y5, y6, y7):
    x = np.logspace(1, 7, num=7, dtype=int)
    plt.plot(x, (y1,y2,y3,y4,y5,y6,y7), marker="o", linestyle="--")
    plt.xscale("log")
    plt.xticks(x, x)
    plt.xlabel("Number of rolls")
    plt.ylabel("Sample mean")
    plt.title("Mean of a six-sided die")
    return plt.show()

def main():
    y1, y2, y3, y4, y5, y6, y7 = dice_rolls()
    rolls_mean(y1, y2, y3, y4, y5, y6, y7)
    print(f"theoretical mean of a dice (six-sided): {dice_mean()}")
    return rolls_mean

if __name__ == "__main__":
    main()