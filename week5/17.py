sentence = input("Enter a sentence: ")

words = sentence.split()

words.reverse()

print("Reversed sentence:", " ".join(words))

# Output:
# Enter a sentence: I am learning Python
# Reversed sentence: Python learning am I