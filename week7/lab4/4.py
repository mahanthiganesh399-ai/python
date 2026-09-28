numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cubes = list(map(lambda x: x ** 3, numbers))

divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Cubes:", cubes)
print("Divisible by 3:", divisible_by_3)