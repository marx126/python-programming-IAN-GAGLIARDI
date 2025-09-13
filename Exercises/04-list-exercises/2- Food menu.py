# Food menu
foods = ["vegetarisk lasagne", "spaghetti", "fisk", "grönsakssoppa", "pannkakor"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Bambameny")
for i in range(len(foods)):
    print(f"{weekdays[i]}: {foods[i]}")

# I knew my solution could be improved. I found how to use zip on internet:
print("\nSecond example")
for day, food in zip(weekdays, foods):
    print(f"{day}: {food}")