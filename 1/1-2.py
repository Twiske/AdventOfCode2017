import fileinput
import re

numbers = fileinput.input(files=('input'))[0]
sum = 0
half = (len(numbers)-1)/2
spacing = int(half - 1)

for x in range(1,10):
    # For each digit find all instances where they are seperated by spacing digits
    # Add in lookahead to have overlapping matches
    p = re.compile(f'{x}(?=.{{{spacing}}}{x})');
    nlist = p.findall(numbers)
    for entry in nlist:
        sum += x * 2 # Multiply by 2 to handle the wrapping


print(sum)


