import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day16.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

class Interval:
    def __init__(self, firstPair, secondPair, name):
        self.low1 = int(firstPair[0])
        self.high1 = int(firstPair[1])
        self.low2 = int(secondPair[0])
        self.high2 = int(secondPair[1])
        self.name = name
        self.index = -1

    def contains(self, num):
        return self.low1 <= num <= self.high1 or self.low2 <= num <= self.high2

    def __eq__(self, other):
        return self.name == other.name

fieldNum = 0
intervals = []
for i in range(0, len(lines)):
    if len(lines[i]) < 2:
        lines = lines[i+1:]
        break
    blocks = lines[i].split(':')
    name = blocks[0]
    blocks = blocks[1].split('or')
    firstPair = blocks[0].strip().split('-')
    secondPair = blocks[1].strip().split('-')
    intervals.append(Interval(firstPair, secondPair, name))
    fieldNum += 1

# Get my ticket
myTicket = [int(c) for c in lines[1].split(',')]
lines = lines[4:]

errorRate = 0
failedLines = []
for l in lines:
    arr = [int(x) for x in l.split(',')]
    failed = False
    for a in arr:
        success = False
        for i in intervals:
            if i.contains(a):
                success = True
                break
        if not success:
            errorRate += a
            failed = True
    if failed:
        failedLines.append(l)

pruned = [[int(c) for c in l.split(',')] for l in lines if l not in failedLines]

possibilities = []
for i in range(0, fieldNum):
    possibilities.append([])
    for j in intervals:
        possibilities[i].append(j)

index = 0
for p in pruned:
    for n in range(0, len(p)):
        failed = []
        for i in possibilities[n]:
            if not i.contains(p[n]):
                failed.append(i)
        for f in failed:
            possibilities[n].remove(f)

noneInterval = Interval([0, 0], [0, 0], None)
determined = [noneInterval for i in range(0, fieldNum)]
while noneInterval in determined:
    for i in range(0, fieldNum):
        if len(possibilities[i]) == 1:
            determined[i] = possibilities[i][0]
        else:
            for d in determined:
                if d in possibilities[i]:
                    possibilities[i].remove(d)

score = 1
for i in range(0, fieldNum):
    if possibilities[i][0].name.split(' ')[0] == 'departure':
        score *= myTicket[i]

print("First: " + str(errorRate))
print("Second: " + str(score))
