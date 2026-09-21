string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in string:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

# Output:
# Enter a string: Hello 123 World
# Vowels: 3
# Consonants: 7
# Digits: 3
# Spaces: 2