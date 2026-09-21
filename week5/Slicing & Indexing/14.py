string = input("Enter a string: ")
substring = input("Enter substring to search: ")

if substring in string:
    print("Substring exists")
else:
    print("Substring does not exist")

# Output:
# Enter a string: Hello Python
# Enter substring to search: Python
# Substring exists