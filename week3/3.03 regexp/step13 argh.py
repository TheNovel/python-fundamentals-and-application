import sys
import re


def line_replace(line):
    return re.sub(r"\b[aA]+\b", "argh", line, 1)


for line in sys.stdin:
    line = line.rstrip()
    print(line_replace(line))
