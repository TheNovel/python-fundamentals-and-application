import sys
import re


def line_check(line):
    return len(re.findall(r"cat", line)) >= 2


for line in sys.stdin:
    line = line.rstrip()
    if line_check(line):
        print(line)
