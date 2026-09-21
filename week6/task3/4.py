import re

text = "Wait!!! What??? Really!!!"

result, count = re.subn(r"([!?])\1+", r"\1", text)

print("Result:", result)
print("Number of replacements:", count)

# Output:
# Result: Wait! What? Really!
# Number of replacements: 3