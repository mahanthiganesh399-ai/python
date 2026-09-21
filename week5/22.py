string = input("Enter a string: ")

for ch in string:
    if string.count(ch) > 1:
        print(ch, ":", string.count(ch))
        break

# Output:
# Enter a string: programming
# r : 2
# g : 2
# m : 2
# r : 2
# g : 2
# m : 2