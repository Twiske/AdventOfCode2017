import fileinput
import re
import sys
import operator
import math
import copy

lines = fileinput.input(files=('input'))
n = 0

bankArray = list(map(int,lines[0].split('\t')))
numBanks = len(bankArray)

bankArrayHistory = [[]]
bankArrayHistory.append(copy.copy(bankArray))

while True:

	n += 1
	bank, blocks = max(enumerate(bankArray), key=operator.itemgetter(1))

	allBanks = math.floor(blocks / numBanks)
	remaining = blocks % numBanks
	bankArray[bank] = 0
	bankAray = [x+allBanks for x in bankArray]
	while remaining > 0:
		bankArray[(bank + remaining) % numBanks] += 1
		remaining -= 1
	if bankArray in bankArrayHistory:
		break;
	#print(bankArray)
	bankArrayHistory.append(copy.copy(bankArray))

print(bankArrayHistory)
print(n)
