# Guess number game
import random

random_number = random.randint(1, 100)
attemps = 0

# Player guesses the number
while True:
    number_choice = int(input("Type a number between 1-100: "))
    if number_choice < random_number:
        attemps += 1
        print("Incorrect, go higher!")
    elif number_choice > random_number:
        attemps += 1
        print("Incorrect, go lower!")
    elif number_choice == random_number:
        attemps += 1
        print(f"Correct! Number of attempts: {attemps}")
        break

# Algorithm to automatically guess the number
print("\nNow the algorithm will try to guess the number!")
low = 1
high = 100
attempts_algo = 0

while low <= high:
    guess = (low + high) // 2
    attempts_algo += 1
    print(f"Algorithm guesses: {guess}")
    
    if guess < random_number:
        print("Go higher!")
        low = guess + 1
    elif guess > random_number:
        print("Go lower!")
        high = guess - 1
    else:
        print(f"Algorithm guessed the number {guess} in {attempts_algo} attempts!")
        break