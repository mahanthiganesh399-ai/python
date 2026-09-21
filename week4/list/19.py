numbers = [10, -5, 20, -8, 30, -2, 40]

result = [0 if num < 0 else num for num in numbers]

print("Original list:", numbers)
print("Updated list:", result)

# Output:
# Original list: [10, -5, 20, -8, 30, -2, 40]
# Updated list: [10, 0, 20, 0, 30, 0, 40]