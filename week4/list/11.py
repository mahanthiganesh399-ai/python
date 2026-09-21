numbers = [30, 10, 20, 40]

# append()
numbers.append(50)
print("After append():", numbers)

# insert()
numbers.insert(1, 15)
print("After insert():", numbers)

# extend()
numbers.extend([60, 70])
print("After extend():", numbers)

# remove()
numbers.remove(15)
print("After remove():", numbers)

# pop()
numbers.pop()
print("After pop():", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# count()
numbers.append(20)
print("After count():", numbers)
print("Count of 20:", numbers.count(20))

# index()
print("Index of 40:", numbers.index(40))

# Output:
# After append(): [30, 10, 20, 40, 50]
# After insert(): [30, 15, 10, 20, 40, 50]
# After extend(): [30, 15, 10, 20, 40, 50, 60, 70]
# After remove(): [30, 10, 20, 40, 50, 60, 70]
# After pop(): [30, 10, 20, 40, 50, 60]
# After sort(): [10, 20, 30, 40, 50, 60]
# After reverse(): [60, 50, 40, 30, 20, 10]
# After count(): [60, 50, 40, 30, 20, 10, 20]
# Count of 20: 2
# Index of 40: 2