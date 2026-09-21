sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:]

result = " ".join(words)

print("Title Case:", result)

# Output:
# Enter a sentence: hello world python programming
# Title Case: Hello World Python Programming