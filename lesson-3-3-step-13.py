import re
import sys

pattern = r"\ba+\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line, re.IGNORECASE):
        print(re.sub(pattern, "argh", line, 1, re.IGNORECASE))
