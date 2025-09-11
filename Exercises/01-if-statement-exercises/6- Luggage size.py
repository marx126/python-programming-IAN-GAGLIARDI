# Luggage size

weight = int(input("Please type the weight of your luggage: "))
length = int(input("Please type the length of your luggage: "))
width = int(input("Please type the width of your luggage: "))
height = int(input("Please type the height of your luggage: "))

if weight > 0 or length > 0 or width > 0 or height > 0:
    if weight < 9 and length < 56 and width < 41 and height < 24:
        (print("Luggage is allowed!"))
print("Invalid luggage!")