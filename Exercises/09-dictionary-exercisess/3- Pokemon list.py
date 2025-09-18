# Pokemon list
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/09-dictionary-exercisess/pokemon_list.txt"
pokedex = {}

with open(file_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        index = parts[0]
        name = parts[1]
        pokemon_type = " ".join(parts[2:])
        pokedex[name] = f"{pokemon_type}, {index}"

print(pokedex["Gengar"])
print(pokedex["Pikachu"])