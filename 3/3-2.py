import fileinput
import re
import sys
import math
from itertools import combinations

def calculateGridValue(x, y):
    sum = 0
    sum += grid[x-1][y]
    sum += grid[x-1][y-1]
    sum += grid[x-1][y+1]
    sum += grid[x]  [y-1]
    sum += grid[x]  [y+1]
    sum += grid[x+1][y]
    sum += grid[x+1][y-1]
    sum += grid[x+1][y+1]

    return sum


lines = fileinput.input(files=('input'))

testValue = int(lines[0])
n = 1
x = 1
y = 0

grid = [[ 0 for xval in range(20) ] for yval in range(20)]
grid[0][0] = 1

while (x < 20):
    grid[x][y] = calculateGridValue(x, y)
    #print(str(x) + " " + str(y))
    if (grid[x][y] > testValue):
        print(str(grid[x][y]))
        break

    leftFilled = grid[x-1][y] != 0
    rightFilled = grid[x+1][y] != 0
    upFilled = grid[x][y+1] != 0
    downFilled = grid[x][y-1] != 0

    if leftFilled and not upFilled:
        y += 1
    if downFilled and not leftFilled:
        x -= 1
    if rightFilled and not downFilled:
        y -= 1
    if upFilled and not rightFilled:
        x += 1

#print(grid)


