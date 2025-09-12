# Guess the number
from random import randint

rand_int = randint(1000, 9999)

for i in range(1000, 10000):
    if i == rand_int:
        print(f"The final guess is: {i}")
print(f"The computer number is: {rand_int}")