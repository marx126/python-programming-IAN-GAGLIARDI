# Encryption
import string
abc = (string.ascii_lowercase)
abc = abc + "ö" + "ä" + "å"
word = input("Please enter a word: ")

encripted_word = ""
for letter in word:
    if letter in abc:
        position = abc.index(letter)
        new_position = position + 1
        encripted_word += abc[new_position]
print(encripted_word)