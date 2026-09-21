import re

def check_password(pw):
    failed = []

    if len(pw) < 8:
        failed.append("Password must be at least 8 characters long")

    if not re.search(r"[A-Z]", pw):
        failed.append("Password must contain at least one uppercase letter")

    if not re.search(r"[a-z]", pw):
        failed.append("Password must contain at least one lowercase letter")

    if not re.search(r"\d", pw):
        failed.append("Password must contain at least one digit")

    if not re.search(r"[!@#$%^&*]", pw):
        failed.append("Password must contain at least one symbol from !@#$%^&*")

    return failed


passwords = [
    "Strong@123",
    "password",
    "PASSWORD123",
    "Pass1234",
    "Abcdefgh"
]

for pw in passwords:
    print("Password:", pw)

    errors = check_password(pw)

    if len(errors) == 0:
        print("Strong password")
    else:
        print("Failed rules:")
        for error in errors:
            print("-", error)

    print()

# Output:
# Password: Strong@123
# Strong password
#
# Password: password
# Failed rules:
# - Password must be at least 8 characters long
# - Password must contain at least one uppercase letter
# - Password must contain at least one digit
# - Password must contain at least one symbol from !@#$%^&*
#
# Password: PASSWORD123
# Failed rules:
# - Password must contain at least one lowercase letter
# - Password must contain at least one symbol from !@#$%^&*
#
# Password: Pass1234
# Failed rules:
# - Password must contain at least one symbol from !@#$%^&*
#
# Password: Abcdefgh
# Failed rules:
# - Password must contain at least one digit
# - Password must contain at least one symbol from !@#$%^&*