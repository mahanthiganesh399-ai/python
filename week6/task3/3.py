import re

text = "I have 3 apples and 5 oranges."

def double_number(match):
    number = int(match.group())
    return str(number * 2)

result = re.sub(r"\d+", double_number, text)

print(result)

# Output:
# I have 6 apples and 10 oranges.