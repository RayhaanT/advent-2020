import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day7.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

class Bag:
    def __init__(self, tag):
        self.tag = tag
        self.holdsGold = 0
        self.inners = []
        self.numbers = []

bags = {}

def parseBag(line):
    split = line.split(' ')       
    outerTag = ' '.join(split[0:2])
    inner = split[4:]

    newBag = Bag(outerTag)
    if outerTag == 'shiny gold':
        newBag.holdsGold = 1

    if inner[0] == 'no':
        return newBag
    for i in range(0, len(inner), 4):
        number = int(inner[i])
        innerTag = ' '.join(inner[i+1:i+3])
        newBag.inners.append(innerTag)
        newBag.numbers.append(number)

    return newBag

def probeGold(bag):
    golds = 0
    for b in bag.inners:
        inner = bags[b]
        if inner.holdsGold:
            golds += inner.holdsGold
            continue
        golds += probeGold(inner)

    bag.holdsGold = golds
    return golds

def countNested(bag):
    total = 1
    for b in range(0, len(bag.inners)):
        inner = bags[bag.inners[b]]
        total += countNested(inner) * bag.numbers[b]
    return total

for l in lines:
    bag = parseBag(l)
    bags[bag.tag] = bag

total = 0
for b in bags.values():
    if probeGold(b):
        total += 1

print("First: " + str(total))
print("Second: " + str(countNested(bags['shiny gold']) - 1))
