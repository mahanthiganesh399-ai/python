num = int(input("Enter a number: "))

temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

average = sum_digits / count

print("Sum of digits:", sum_digits)
print("Average of digits:", average)

# Output:
# Enter a number: 1234
# Sum of digits: 10
# Average of digits: 2.5