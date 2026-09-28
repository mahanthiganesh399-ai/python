students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]

result = sorted(students, key=lambda s: s[1], reverse=True)

print(result)