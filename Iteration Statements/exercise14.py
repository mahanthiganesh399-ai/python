n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)

# Output:
# Enter a number: 5
# Factorial: 120