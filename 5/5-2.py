import fileinput
import re
import sys

lines = fileinput.input(files=('input'))

n = 0
sum = 0

instructionArray = list(map(int,lines))

while n >= 0 and n < len(instructionArray):
    jumpValue = instructionArray[n]
    if jumpValue >= 3:
        instructionArray[n] -= 1
    else:
        instructionArray[n] += 1
    n += jumpValue
    sum += 1

print(sum)


