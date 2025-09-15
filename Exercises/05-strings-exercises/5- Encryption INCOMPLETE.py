# Encryption
import string
abc = (string.ascii_lowercase)
abc = abc + "ö" + "ä" + "å"
word = input("Please enter a word: ")
lower_word = word.lower
encripted_word = ""

for letter in word:
    if letter in abc:
        position = abc.index(letter)
        print(position)
