import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"(cat).*?\1"
    if re.match(pattern, line) is not None:
        print(line)
