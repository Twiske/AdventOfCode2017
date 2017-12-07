import fileinput
import re
import sys
import math
from itertools import combinations

# Calculate the values residing on the 4 axes
def calculateAxisNumber(n):
    return math.ceil((n*n + n + 2.0) / 4.0)

lines = fileinput.input(files=('input'))

testValue = int(lines[0])
n = 1

lastAxisDistance = testValue
while True:
    axisNumber = calculateAxisNumber(n)
    axisDistance = abs(axisNumber - testValue)
    print(axisDistance)
    if axisDistance > lastAxisDistance:
        # Passed the minimum so n-1 must be closest axis
        print(lastAxisDistance + math.ceil((n-2)/4))
        break
    lastAxisDistance = axisDistance
    n += 1



