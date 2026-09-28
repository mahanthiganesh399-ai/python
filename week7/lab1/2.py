def simple_interest(principal, rate, time):
    """Calculates simple interest."""
    return (principal * rate * time) / 100

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = simple_interest(principal, rate, time)

print("Simple Interest:", si)

# Output:
# Enter principal: 5000
# Enter rate: 5
# Enter time: 2
# Simple Interest: 500.0