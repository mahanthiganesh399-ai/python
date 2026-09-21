string = input("Enter a string: ")
ch = input("Enter the character: ")

first = string.find(ch)
last = string.rfind(ch)

print("First occurrence index:", first)
print("Last occurrence index:", last)

# Output:
# Enter a string: banana
# Enter the character: a
# First occurrence index: 1
# Last occurrence index: 5