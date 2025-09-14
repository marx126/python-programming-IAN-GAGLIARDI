# Counting words

sentence = "A picture says more than a thousand words, a matematical formula says more than a thousand pictures."
clean_sentence = sentence.replace(",", "").replace(".", "").split() # Cant handle special characters
print(len(clean_sentence))