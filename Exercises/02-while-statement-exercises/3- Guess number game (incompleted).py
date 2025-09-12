# Guess number game
import random

random_number = random.randint(1,100)
attemps = 0

while True:
    number_choice = int(input("Type a number between 1-100: "))
    if number_choice < random_number:
        attemps += 1
        print("Incorrect, go higer!")
    elif number_choice > random_number:
        attemps += 1
        print("incorrect, go lower!")
    elif number_choice == random_number:
        attemps += 1
        print(f"Correct!, number of attemps: {attemps}")
        break

# ALGORITHM TO AUTOMATICALLY GUESS THE NUMBER IS MISSING, EXERCISE IS NOT COMPLETED!