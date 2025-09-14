# Vowels
vowels = "aeiou" # Not including y as a vowel

sentence = "Pure mathematics is, in its way, the poetry of logical ideas"
vowels = "aeiou"
count = 0
for letter in sentence:
    if letter in vowels:
        count += 1

print(f"There are {count} vowels in this sentence")

# It can also be written this way
total_vowels = sum(1 for letter in sentence if letter in vowels)