import sys
import re


def line_check(line):
    return re.search(r"\b(\w+)\1\b", line)


for line in sys.stdin:
    line = line.rstrip()
    if line_check(line):
        print(line)
