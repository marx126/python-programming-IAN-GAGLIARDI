# Dice rolls convergence
from random import randint
import matplotlib.pyplot as plt

# A
dice_roll = [randint(1, 6) for i in range(100)]
print(f"The number of outcome six in 100 dice rolls is: {dice_roll.count(6)}\n")

# B
rolls_list = [10, 100, 1000, 10000, 100000, 1000000]
six_count = []
probabilities = []
for rolls in rolls_list:
    result = [randint(1,6) for i in range(rolls)]

    count_six = result.count(6)
    six_count.append(count_six)

    probability = count_six/rolls
    probabilities.append(probability)

# C
plt.plot(probabilities, '-*')
plt.title("Probability of six for different number of rolls")
plt.xticks([0,1,2,3,4,5], rolls_list);
plt.xlabel("Number of dice rolls")
plt.ylabel("Probability")
plt.show()