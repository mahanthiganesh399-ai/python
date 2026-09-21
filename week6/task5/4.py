import re

def clean_text(html):
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", html)

    # Replace multiple spaces, tabs and newlines with one space
    text = re.sub(r"\s+", " ", text)

    # Remove spaces from beginning and end
    return text.strip()

html = """
<html>
    <body>
        <h1>Welcome</h1>
        <p>This is    a test.</p>
        <p>Python    Regular Expressions</p>
    </body>
</html>
"""

result = clean_text(html)

print(result)

# Output:
# Welcome This is a test. Python Regular Expressions