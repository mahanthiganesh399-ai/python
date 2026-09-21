import re

text = "Contact us at john@gmail.com or support@example.com for help."

result = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)

print(result)

# Output:
# Contact us at [EMAIL HIDDEN] or [EMAIL HIDDEN] for help.