n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# Output:
# Enter number of rows: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5