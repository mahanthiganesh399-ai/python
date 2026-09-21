import re

# Task 6 - Mini Log Parser

log = """[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"
"""

# Pattern with named groups
pattern = r'\[(?P<time>.*?)\] (?P<level>\w+) user=(?P<user>\w+) msg="(?P<msg>.*?)"'

entries = []

# Find all log entries
for match in re.finditer(pattern, log):
    entries.append(match.groupdict())

print("Log Entries:")

for entry in entries:
    print(entry)

# Count ERROR, WARN and INFO
error = 0
warn = 0
info = 0

for entry in entries:
    if entry["level"] == "ERROR":
        error += 1
    elif entry["level"] == "WARN":
        warn += 1
    elif entry["level"] == "INFO":
        info += 1

print("\nSummary:")
print("ERROR:", error)
print("WARN:", warn)
print("INFO:", info)

# Hide usernames
redacted = re.sub(r"user=\w+", "user=<hidden>", log)

print("\nRedacted Log:")
print(redacted)

# Output:
# Log Entries:
# {'time': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'}
# {'time': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'}
# {'time': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}
#
# Summary:
# ERROR: 1
# WARN: 1
# INFO: 1
#
# Redacted Log:
# [2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
# [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
# [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"