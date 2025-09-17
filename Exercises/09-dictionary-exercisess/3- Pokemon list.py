# Pokemon list
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/09-dictionary-exercisess/pokemon_list.txt"
with open(file_path, "r") as f:
    pokemon_list = f.readlines()

for i in pokemon_list:
    print(i.strip())