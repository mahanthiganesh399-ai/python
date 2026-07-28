import sys

if len(sys.argv) != 3:
    print("Usage: python sum.py num1 num2")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum =", num1 + num2)

#output
#python sum.py 10 20
#Sum = 30
#
#python sum.py 10
#Usage: python sum.py num1 num2