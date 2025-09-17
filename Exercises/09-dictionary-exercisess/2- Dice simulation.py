# Dice simulation
import random
dice_rolls = [random.randint(1,6) for i in range(1_000_000)]

total_rolls = {i: 0 for i in range(1,7)}

for roll in dice_rolls:
    total_rolls[roll] += 1

for number, count in total_rolls.items():
    print(f"{number}: {count}")