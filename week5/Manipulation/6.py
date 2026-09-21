string = input("Enter a string: ")
ch = input("Enter the character to count: ")

count = 0

for i in string:
    if i == ch:
        count += 1

print("Occurrences:", count)

# Output:
# Enter a string: banana
# Enter the character to count: a
# Occurrences: 3