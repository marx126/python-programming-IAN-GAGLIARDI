# Encryption
import string
abc = list(string.ascii_lowercase)
abc.extend(["ö", "ä", "å"])

word = input("Please enter a word: ")
lower_word = word.lower
encripted_word = ""

for i in word:
    if i in abc:
