import re

paragraph = "NASA and USA worked with ISRO to launch a satellite successfully."

for match in re.finditer(r"\b[A-Za-z]{7,}\b", paragraph):
    print("Word:", match.group(), "Start index:", match.start())

# Output:
# Word: satellite Start index: 38
# Word: successfully Start index: 48