# Smallest

n1 = float(input("Please, type any number: "))
n2 = float(input("Please type another number: "))

if n1 > n2:
    print(f"{n1} is greater than {n2}!")
elif n2 > n1:
    print(f"{n2} is greater than {n1}!")
else:
    print(f"{n1} and {n2} are equal!")