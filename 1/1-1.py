import fileinput
import re

numbers = fileinput.input(files=('input'))[0]
sum = 0

p = [None] * 10
for x in range(1,10):
    p = re.compile(f'{x}{{2,}}');
    nlist = p.findall(numbers)
    for entry in nlist:
        sum += (len(entry) - 1) * x

if numbers[len(numbers)-2] == numbers[0]:
    sum += int(numbers[0])

print(sum)


