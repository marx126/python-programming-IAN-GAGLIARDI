# Counting letters

word = input("Type a word: ")

upper_count = sum(1 for char in word if char.isupper())
lowe_count = sum(1 for char in word if char.islower())

print(f"Number of letters in the word?: {len(word)}")
print(f"Number of upper cases: {upper_count}")
print(f"Number of lower cases. {lowe_count}")