import re
import sys

pattern = r"(cat).*?\1"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line) is not None:
        print(line)
