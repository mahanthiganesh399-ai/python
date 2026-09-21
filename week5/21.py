string = input("Enter a string: ")

if string.isdigit():
    print("Only digits")
elif string.isalpha():
    print("Only alphabets")
elif string.isalnum():
    print("Alphanumeric")
else:
    print("Contains special characters")

# Output:
# Enter a string: 12345
# Only digits

# Output:
# Enter a string: Hello
# Only alphabets

# Output:
# Enter a string: Hello123
# Alphanumeric

# Output:
# Enter a string: Hello@123
# Contains special characters