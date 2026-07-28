a = 10
b = 20

print("Before swapping:", a, b)

temp = a
a = b
b = temp

print("After swapping using temporary variable:", a, b)

a = 10
b = 20

a, b = b, a

print("After swapping using tuple unpacking:", a, b)

#output
#Before swapping: 10 20
#After swapping using temporary variable: 20 10
#After swapping using tuple unpacking: 20 10