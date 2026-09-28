from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda x: x % 2 == 0, nums)

squares = map(lambda x: x ** 2, evens)

total = reduce(lambda a, b: a + b, squares)

print("Total:", total)