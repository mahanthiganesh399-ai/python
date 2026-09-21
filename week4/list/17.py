words = ["apple", "cat", "banana", "dog", "orange", "book"]

long_words = [word for word in words if len(word) > 4]

print("Words with more than 4 letters:", long_words)

# Output:
# Words with more than 4 letters: ['apple', 'banana', 'orange']