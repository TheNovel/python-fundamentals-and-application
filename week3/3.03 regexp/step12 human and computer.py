import sys
import re


def line_replace(line):
    return re.sub(r"(human)", "computer", line)


for line in sys.stdin:
    line = line.rstrip()
    print(line_replace(line))