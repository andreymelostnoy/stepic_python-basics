import re
import sys

pattern = r"human"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, "computer", line))
