# Right angle

a = int(input("Please type an angle: "))
b = int(input("Please type a second angle: "))
c = int(input("Please type a third angle: "))

total = a + b + c

if a > 0 and b > 0 and c > 0 and total == 180: # Check if all numbers are positive
    if a == 90 or b == 90 or c == 90:
        print("Your triangle has a right angle!")
else:
    print("Your triangle has NOT a right angle!")