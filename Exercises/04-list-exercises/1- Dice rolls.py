# Dice rolls
import random

my_list = []

# Using append:
for i in range(10):
    my_list.append(random.randint(1,6))

print(f"Ascending order: {sorted(my_list)}\n")
print(f"Descending order: {sorted(my_list, reverse=True)}\n")
print(f"Maximum. {max(my_list)}\n")
print(f"Minimum: {min(my_list)}")

my_list = my_list.sort

# Using list comprehension:
my_list2 = [random.randint(1, 6) for i in range(10)]