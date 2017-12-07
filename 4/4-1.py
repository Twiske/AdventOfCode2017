import fileinput
import re
import sys

lines = fileinput.input(files=('input'))

sum = 0

for line in lines:
    lineList = line.rstrip().split(" ")
    lineSet = set(lineList)

    print(lineList)
    print(lineSet)
    print("\n")
    if len(lineSet) == len(lineList):
        sum += 1

print(sum)


