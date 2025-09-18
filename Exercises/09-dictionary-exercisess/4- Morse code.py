# Morse code
file_path = "/Users/ianpablogagliardibianchini/Projects/python-programming-IAN-GAGLIARDI/Exercises/09-dictionary-exercisess/morse.txt"

morse_dic = {}
with open(file_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        letter = parts[0]
        letter = letter[0]
        morse = parts[1]
        morse_dic[letter] = morse

def morse(my_string: str):
    big_string = my_string.upper()
    morse_translation = ""
    for i in big_string:
        if i in morse_dic:
            morse_translation += morse_dic[i]
    return morse_translation

print(morse("sos"))
print(morse("POKEMON"))
