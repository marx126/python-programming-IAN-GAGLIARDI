# Multiplication game
import random

score = 0

while True:
    easy_num1 = random.randint(1, 10)
    easy_num2 = random.randint(1, 10)
    medium_num1 = random.randint(10, 100)
    medium_num2 = random.randint(1, 10)
    hard_num1 = random.randint(10, 100)
    hard_num2 = random.randint(10, 100)

    difficulty = int(input("""Choose a difficulty.
1 = easy
2 = medium
3 = hard
"""))

    if difficulty == 1:
        answer = int(input(f"What is the result of {easy_num1} times {easy_num2}?: "))

        if answer == easy_num1 * easy_num2:
            score += 1
            print("Good work!")
        else:
            print(f"Wrong answer! The result of {easy_num1} times {easy_num2} is: {easy_num1 * easy_num2}")
    
        end = int(input("Press 1 to play again or 0 to end."))

        if end == 0:
            print(f"Thanks for playing, your total score was: {score}")
            break

    elif difficulty == 2:
        answer = int(input(f"What is the result of {medium_num1} times {medium_num2}?: "))

        if answer == medium_num1 * medium_num2:
            score += 1
            print("Good work!")
        else:
            print(f"Wrong answer! The result of {medium_num1} times {medium_num2} is: {medium_num1 * medium_num2}")
    
        end = int(input("Press 1 to play again or 0 to end."))

        if end == 0:
            print(f"Thanks for playing, your total score was: {score}")
            break
    
    elif difficulty == 3:
        answer = int(input(f"What is the result of {hard_num1} times {hard_num2}?: "))

        if answer == hard_num1 * hard_num2:
            score += 1
            print("Good work!")
        else:
            print(f"Wrong answer! The result of {hard_num1} times {hard_num2} is: {hard_num1 * hard_num2}")
    
        end = int(input("Press 1 to play again or 0 to end."))

        if end == 0:
            print(f"Thanks for playing, your total score was: {score}")
            break