import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day15.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

starters = [int(x) for x in lines[0].split(',')]
mostRecent = {}

for s in range(1, len(starters)):
    mostRecent[starters[s - 1]] = s

TURNS = 30000000
last = starters[-1]
for i in range(len(starters), TURNS):
    original = last
    if last in mostRecent.keys():
        last = i - mostRecent[last]
    else:
        last = 0
    mostRecent[original] = i
print(last)
