import sys
import re


def division_checker(line):
    return re.match(r"(1(01*0)*1|0)*$", line)


for line in sys.stdin:
    line = line.rstrip()
    if division_checker(line):
        print(line)
