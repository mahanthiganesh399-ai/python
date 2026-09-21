import re

sentence = "I have a cat and a dog. My friend has a bird and another cat."

pattern = r"\b(cat|dog|bird)\b"

matches = re.findall(pattern, sentence)

print("Pets found:", matches)

# Output:
# Pets found: ['cat', 'dog', 'bird', 'cat']