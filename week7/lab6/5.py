from functools import reduce

employees = [
    {"name": "Ravi", "department": "CSE", "salary": 30000},
    {"name": "Sita", "department": "ECE", "salary": 35000},
    {"name": "Amit", "department": "CSE", "salary": 40000},
    {"name": "Priya", "department": "CSE", "salary": 45000},
    {"name": "Rahul", "department": "ECE", "salary": 38000}
]

department = "CSE"

selected = filter(lambda e: e["department"] == department, employees)

hiked = map(
    lambda e: {
        "name": e["name"],
        "department": e["department"],
        "salary": e["salary"] * 1.10
    },
    selected
)

hiked_employees = list(hiked)

total_salary = reduce(
    lambda a, b: a + b["salary"],
    hiked_employees,
    0
)

print("Employees after 10% hike:")

for employee in hiked_employees:
    print(employee)

print("Total salary expenditure:", total_salary)