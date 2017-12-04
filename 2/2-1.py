import fileinput
import re
import sys

lines = fileinput.input(files=('input'))
sum = 0


for line in lines:
    min = 1000000
    max = 0
    for value in list(map(int,line.split("\t"))):
        max = value if value > max else max
        min = value if value < min else min
    sum+= max - min



print(sum)


