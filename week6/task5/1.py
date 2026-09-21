import re

def is_valid_email(s):
    pattern = r"^[\w.]+@[\w.-]+\.[A-Za-z]{2,6}$"
    return re.fullmatch(pattern, s) is not None

emails = [
    "john@gmail.com",
    "user.name@yahoo.com",
    "abc123@college.edu",
    "test@mail.co",
    "a@b.c",
    "a\\@b.c",
    "no-at-sign.com",
    "user@gmail"
]

for email in emails:
    print(email, "->", is_valid_email(email))

# Output:
# john@gmail.com -> True
# user.name@yahoo.com -> True
# abc123@college.edu -> True
# test@mail.co -> True
# a@b.c -> False
# a\@b.c -> False
# no-at-sign.com -> False
# user@gmail -> False