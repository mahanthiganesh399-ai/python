def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = gcd(a, b)

lcm = (a * b) // g

print("GCD:", g)
print("LCM:", lcm)