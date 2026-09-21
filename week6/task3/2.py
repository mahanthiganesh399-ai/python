import re

text = "Doe, John"

result = re.sub(r"(\w+),\s*(\w+)", r"\2 \1", text)

print(result)

# Output:
# John Doe