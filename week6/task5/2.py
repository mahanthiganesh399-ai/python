import re

text = """
Call 555-123-4567 or (555) 987-6543.
You can also reach us at 555.222.3333.
"""

pattern = r"(?:\(\d{3}\)|\d{3})[-.\s]\d{3}[-.]\d{4}"

numbers = re.findall(pattern, text)

print("Original numbers:")

for number in numbers:
    print(number)

print("\nNormalized numbers:")

for number in numbers:
    normalized = re.sub(r"\D", "", number)
    normalized = re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", normalized)
    print(normalized)

# Output:
# Original numbers:
# 555-123-4567
# (555) 987-6543
# 555.222.3333
#
# Normalized numbers:
# 555-123-4567
# 555-987-6543
# 555-222-3333