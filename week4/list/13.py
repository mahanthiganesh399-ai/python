numbers = [10, 25, 5, 40, 15]

maximum = numbers[0]
minimum = numbers[0]
total = 0

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    total = total + num

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)

# Output:
# Maximum: 40
# Minimum: 5
# Sum: 95