year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31

    if day >= 1 and day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")

# Output:
# Enter year: 2024
# Enter month: 2
# Enter day: 29
# Valid date