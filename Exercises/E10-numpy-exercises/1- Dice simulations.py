# Dice simulations
import numpy as np
import random

def dice_mean(): # Function to call the theoretical mean of a dice
    dice_faces = np.arange(1,7)
    return dice_faces.mean()

print(dice_mean())
many_dices = np.random.randint(1,6,10)
print(many_dices)
