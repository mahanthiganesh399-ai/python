import re

text = "Important dates are 21/09/2026, 05/10/2026 and 15/12/2026."

pattern = r"(\d{2})/(\d{2})/(\d{4})"

dates = re.findall(pattern, text)

print("Extracted dates:")

for date in dates:
    print(date)

result = re.sub(pattern, r"\3-\2-\1", text)

print("\nReformatted text:")
print(result)

# Output:
# Extracted dates:
# ('21', '09', '2026')
# ('05', '10', '2026')
# ('15', '12', '2026')
#
# Reformatted text:
# Important dates are 2026-09-21, 2026-10-05 and 2026-12-15.