# Medicine

age = int(input("Please type your age: "))
weight = float(input("Please type your weight: "))

if age > 12 and weight > 40:
    print("Number of recomended pills: 1-2")
elif age > 6 and weight > 25:
    print("Number of recommended pills: 1/2-1")
elif age > 2 and weight > 14:
    print("Number of recommended pills: 1/2")
else:
    print("Invalid age/weight ratio.")