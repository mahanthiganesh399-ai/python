import re

pattern = r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?"

colors = ["#FFAA00", "#000", "#12AB", "#GGG"]

for color in colors:
    if re.fullmatch(pattern, color):
        print(color, "is a valid hexadecimal color")
    else:
        print(color, "is not a valid hexadecimal color")

# Output:
# #FFAA00 is a valid hexadecimal color
# #000 is a valid hexadecimal color
# #12AB is not a valid hexadecimal color
# #GGG is not a valid hexadecimal color