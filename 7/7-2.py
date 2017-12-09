import fileinput
import re
import sys
import operator
import math
import copy

class Node:
    def __init__(self, weight, children):
        self.weight = int(weight)
        self.children = children
        self.parent = None


lines = fileinput.input(files=('input'))

parseRegex = re.compile('(.+) \((\d+)\)(?: -> )?(.+)?')

nodes = {}

def calcWeight(name):
    sum = nodes[name].weight
    print(nodes[name].children)
    for child in nodes[name].children:
        addedWeight = nodes[child].weight
        #addedWeight += calcWeight(child)
        sum += addedWeight

    return sum

for line in lines:
    matches = parseRegex.match(line)

    name = matches.group(1)
    weight = matches.group(2)
    if (matches.group(3) != None):
        children = matches.group(3).split(", ")
    else:
        children = []
    print(name + " " + weight + " " + str(children))

    nodes[name] = Node(weight, children)

for key, value in nodes.items():
    if value.children != []:
        print(key)
        for child in value.children:
            print(calcWeight(child))
        print()


