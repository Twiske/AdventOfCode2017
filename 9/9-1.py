import fileinput
import re
import sys
import operator
import math
import copy


lines = fileinput.input(files=('input'))

score = 0
currentDepth = 0

inGarbage = False
skipNext = False
for c in lines[0]:

    if skipNext:
        skipNext = False
        continue

    if not inGarbage:
        if c == "{":
            currentDepth += 1
            score += currentDepth
        elif c == "}":
            currentDepth -= 1
        elif c == "<":
            inGarbage = True
    else:
        if c == "!":
            skipNext = True
        elif c == ">":
            inGarbage = False

    


print(score)
