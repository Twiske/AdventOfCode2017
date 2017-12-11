import fileinput
import re
import sys
import operator
import math
import copy


lines = fileinput.input(files=('input'))
lengths = list(map(int,lines[0].split(",")))

skipSize = 0

print(str(lengths))
knots = list(range(1,255))

for length in lengths:
    knots[0:length] = knots[0:length][::-1]
    shiftAmmount = length + skipSize
    knots = knots[-shiftAmmount:] + knots[:-shiftmAmount]
    skipSize += 1


print(knots)
