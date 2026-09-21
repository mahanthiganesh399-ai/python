import re

paragraph = "NASA and USA worked with ISRO to launch a new satellite. ISRO is based in INDIA."

words = re.findall(r"\b[A-Z]{2,}\b", paragraph)

print("Capital words:", words)

# Output:
# Capital words: ['NASA', 'USA', 'ISRO', 'ISRO', 'INDIA']