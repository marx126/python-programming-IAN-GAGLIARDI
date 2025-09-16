# Dice rolls
from random import randint
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/08-file-handling-exercises/dice_rolls.txt"

with open(file_path, "w") as f:
    dice_rolls = [randint(1, 6) for i in range(20)]
    f.write("Simulate 20 dice rolls:\n")
    f.write(" ".join(str(roll) for roll in dice_rolls) + "\n")

    f.write("\nSorted dice rolls:\n")
    f.write(" ".join(str(roll) for roll in sorted(dice_rolls)) + "\n")

    f.write(f"\nNumber of fours: {dice_rolls.count(4)}")
