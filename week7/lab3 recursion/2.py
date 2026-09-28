def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 15 Fibonacci terms:")
n=int(input("enter the value"))

for i in range(n):
    print(fibonacci(i), end=" ")
