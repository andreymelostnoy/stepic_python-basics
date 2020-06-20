import re
import sys

pattern = r"\b(\w+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) is not None:
        print(line)
