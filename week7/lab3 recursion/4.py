def power(base, exp):
    if exp == 0:
        return 1

    if exp < 0:
        return 1 / power(base, -exp)

    return base * power(base, exp - 1)

base = float(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result:", power(base, exp))