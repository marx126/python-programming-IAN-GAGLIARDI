# Divisible

num = int(input("Type any number: "))

if num % 5 == 0 and num % 2 != 0:
    print(f"{num} is odd and divisible by 5")
elif num % 5 == 0 and num % 2 == 0:
    print(f"{num} is even and divisible by 5.")
elif num % 5 != 0 and num % 2 == 0:
    print(f"{num} is even but not divisible by 5")
else:
    print(f"{num} is odd but not divisible by 5")