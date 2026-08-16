start = int(input("Enter starting limit: "))
end = int(input("Enter ending limit: "))

print("Prime numbers:")

for num in range(start, end + 1):
    if num >= 2:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")

# Output:
# Enter starting limit: 10
# Enter ending limit: 30
# Prime numbers:
# 11 13 17 19 23 29