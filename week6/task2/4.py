import re

text = "apple banana apple mango apple orange"

matches = re.findall(r"apple", text)

print("Matches:", matches)
print("Number of occurrences:", len(matches))

# Output:
# Matches: ['apple', 'apple', 'apple']
# Number of occurrences: 3