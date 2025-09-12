# Multiplication table

# A)
value = 6
for i in range(0, 11):
    value = 6 * i
    print(value, end=" ")
print()

# B)
table = int(input("\nWhich table are you interested in?: "))
start = int(input("Specify start of table: "))
end = int(input("Specify end of table: "))
print(f"\nYour {table}th multiplication table from {start} to {end}:")
for i in range(start, end + 1):
    print(table * i, end=" ")
print("\n")

# C)
print("Full multiplication table from 0 to 10:")
for i in range(0, 11):
    for j in range(0, 11):
        print(f"{j*i :4}", end="")
    print()