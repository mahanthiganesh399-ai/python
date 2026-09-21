string = input("Enter a string: ")
old = input("Enter character/word to replace: ")
new = input("Enter new character/word: ")

result = string.replace(old, new)

print("Updated string:", result)

# Output:
# Enter a string: I like Java
# Enter character/word to replace: Java
# Enter new character/word: Python
# Updated string: I like Python