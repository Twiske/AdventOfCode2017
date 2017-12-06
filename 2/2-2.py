import fileinput
import re
import sys
from itertools import combinations

lines = fileinput.input(files=('input'))
sum = 0


for line in lines:

    intlist = list(map(int,line.split("\t")))
    intlist = sorted(intlist, reverse=True)

    for combo in combinations(intlist, 2):
        if (combo[0] % combo[1] == 0):
            sum += combo[0] / combo[1]
            break;




print(sum)


