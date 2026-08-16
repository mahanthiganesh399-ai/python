num = int(input("Enter a number: "))

reverse = 0
temp = num

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reversed number:", reverse)

# Output:
# Enter a number: 1234
# Reversed number: 4321