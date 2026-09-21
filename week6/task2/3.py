import re

prices = "apples: $3.50, bananas: $1.20, mango: $4.75"

amounts = re.findall(r"\$\d+\.\d+", prices)

print("Dollar amounts:", amounts)

# Output:
# Dollar amounts: ['$3.50', '$1.20', '$4.75']