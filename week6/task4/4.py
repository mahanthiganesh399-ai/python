import re

log = "2024-06-01 08:15:32 ERROR Disk full"

pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.*)"

m = re.fullmatch(pattern, log)

print("Date:", m.group("date"))
print("Time:", m.group("time"))
print("Level:", m.group("level"))
print("Message:", m.group("message"))

# Output:
# Date: 2024-06-01
# Time: 08:15:32
# Level: ERROR
# Message: Disk full