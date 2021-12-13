import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day5.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

def stringToInt(s):
    width = len(s.strip())
    out = 0
    for x in range(0, width):
        if s[x] == 'B' or s[x] == 'R':
            out += 2**(width - x - 1)
    return out

highest = 0
allIds = []
for l in lines:
    row = stringToInt(l[0:7])
    column = stringToInt(l[7:])
    allIds.append(row * 8 + column)

allIds.sort()
highest = allIds[-1]

print("First: " + str(highest))

gap = 0
for i in range(1, len(allIds)):
    if allIds[i] - allIds[i - 1] == 2:
        print("Second: " + str(allIds[i] - 1))
        break
