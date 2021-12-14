import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day9.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

def isSumOne(n, preamble):
    table = [False for i in range(0, n)]
    for x in preamble:
        if x >= n:
            continue
        if table[x]:
            return True
        table[n - x] = True
    return False

def isSumTwo(n, preamble):
    for x in range(0, len(preamble)):
        for y in range(x + 1, len(preamble)):
            if preamble[x] + preamble[y] == n:
                return True
    return False

def findSequence(n, lst):
    for i in range(0, len(lst) - 1):
        seq = [lst[i]]
        for j in range(i + 1, len(lst) - 1):
            seq.append(lst[j])
            if sum(seq) == n:
                return seq
            if sum(seq) > n:
                break
    return []

PREAMBLE_LENGTH = 25

preamble = [int(lines[i]) for i in range(0, PREAMBLE_LENGTH)]

vulnerable = 0
for i in range(PREAMBLE_LENGTH, len(lines)):
    if not isSumTwo(int(lines[i]), preamble):
        print("First: " + lines[i])
        vulnerable = int(lines[i])
        break
    preamble = preamble[1:]
    preamble.append(int(lines[i]))

allNums = [int(l) for l in lines]

seq = findSequence(vulnerable, allNums)
seq.sort()
print("Second: " + str(seq[0] + seq[-1]))
