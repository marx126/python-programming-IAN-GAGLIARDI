# Encryption
import string
abc = (string.ascii_lowercase)
abc = abc + "ö" + "ä" + "å"

choice = int(input("press 1 to encryption or 2 to decryption: "))
word = input("Please enter a word: ")

encrypted_word = ""
decrypted_word = "" 
for letter in word:
    if letter in abc:
        position = abc.index(letter)
        if choice == 1:
            if position == len(abc) -1:
                new_position = 0
            else:
                new_position = position + 1
            encrypted_word += abc[new_position]
        elif choice == 2:
            if position == 0:
                new_position = len(abc) - 1
            else:
                new_position = position - 1
            decrypted_word += abc[new_position]

# Probably not the cleanest code but it works