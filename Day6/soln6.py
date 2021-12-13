import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day6.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

groups = []
currentGroup = ''
for l in lines:
    if len(l) == 0:
        groups.append(currentGroup)
        currentGroup = ''
    for c in l:
        if c not in currentGroup:
            currentGroup += c

groups.append(currentGroup)

total = 0
for g in groups:
    total += len(g)

print("First: " + str(total))

groups = []
currentGroup = ''
first = True
skip = False
for l in lines:
    if len(l) == 0:
        groups.append(currentGroup)
        currentGroup = ''
        first = True
        skip = True
    if skip:
        skip = False
        continue
    if first:
        currentGroup = l
        first = False
        continue
    for c in currentGroup:
        if c not in l:
            currentGroup = currentGroup.replace(c, "")

groups.append(currentGroup)

total = 0
for g in groups:
    total += len(g)

print("Second: " + str(total))
