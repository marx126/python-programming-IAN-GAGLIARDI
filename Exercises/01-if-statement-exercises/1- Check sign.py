# Check sign

number = (float(input("Please type any number: "))) # Decimals are allowed

if number > 0:
    print(f"{number} is a positive number!")
elif number < 0:
    print(f"{number} is a negative number!")
else:
    print(f"{number} is zero!")