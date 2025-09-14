# Palindrome
sentence = input("Write a sentence: ")
clean_sentence = sentence.replace(" ","").lower()

if clean_sentence == clean_sentence[::-1]:
    print(f"{sentence} is a palindrome.")
else:
    print(f"{sentence} is not a palindrome.")