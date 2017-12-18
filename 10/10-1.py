import fileinput
import re
import sys
import operator
import math
import copy


lines = fileinput.input(files=('input'))
lengths = list(map(int,lines[0].split(",")))

skipSize = 0
totalShift = 0

print(str(lengths))
knots = list(range(0,256))
print(knots)
for length in lengths:
    knots[0:length] = knots[0:length][::-1]
    shiftAmmount = (length + skipSize) % len(knots)
    knots = knots[shiftAmmount:] + knots[:shiftAmmount]
    totalShift += shiftAmmount
    skipSize += 1
    print("After length: " +  str(length) + " " + str(knots))
#print(knots)
totalShift = totalShift % len(knots)
knots = knots[-totalShift:] + knots[:-totalShift]
print(totalShift)
print(knots)
print(knots[0] * knots[1])
