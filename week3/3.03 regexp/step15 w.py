import sys
import re


def line_replace(line):
    return re.sub(r'(\w)\1*', r'\1', line)


for line in sys.stdin:
    line = line.rstrip()
    print(line_replace(line))
