import time
import copy
import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day11.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

def getNeighbours(field, x, y):
    left = x - 1 if x > 0 else None
    right = x + 1 if x < len(field[0]) - 1 else None
    up = y - 1 if y > 0 else None
    down = y + 1 if y < len(field) - 1 else None

    neighbours = []

    if left is not None:
        neighbours.append(field[y][left])
    if right is not None:
        neighbours.append(field[y][right])
    if up is not None:
        neighbours.append(field[up][x])
    if down is not None:
        neighbours.append(field[down][x])
    if left is not None and up is not None:
        neighbours.append(field[up][left])
    if left is not None and down is not None:
        neighbours.append(field[down][left])
    if right is not None and up is not None:
        neighbours.append(field[up][right])
    if right is not None and down is not None:
        neighbours.append(field[down][right])

    return neighbours

def getDeepNeighbours(field, x, y):
    neighbours = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == dx == 0:
                continue
            n = lineOfSight(field, x + dx, y + dy, dx, dy)
            if n is not None:
                neighbours.append(n)
    return neighbours

def lineOfSight(field, startX, startY, slopeX, slopeY):
    x = startX
    y = startY
    height = len(field)
    width = len(field[0])
    while 0 <= x < width and 0 <= y < height:
        if field[y][x] != '.':
            return field[y][x]
        x += slopeX
        y += slopeY
    return None

def count(neighbours, key):
    total = 0
    for n in neighbours:
        if n == key:
            total += 1
    return total

def occupied(field):
    total = 0
    for r in field:
        for s in r:
            if s == '#':
                total += 1
    return total

def update(field):
    updated = []
    for y in range(0, len(field)):
        updated.append([])
        for x in range(0, len(field[y])):
            new = field[y][x]
            neighbours = getNeighbours(field, x, y)
            if field[y][x] == '#' and count(neighbours, '#') >= 4:
                new = 'L'
            if field[y][x] == 'L' and count(neighbours, '#') == 0:
                new = '#'
            updated[y].append(new)
    return updated

def deepUpdate(field):
    updated = []
    for y in range(0, len(field)):
        updated.append([])
        for x in range(0, len(field[y])):
            new = field[y][x]
            neighbours = getDeepNeighbours(field, x, y)
            if field[y][x] == '#' and count(neighbours, '#') >= 5:
                new = 'L'
            if field[y][x] == 'L' and count(neighbours, '#') == 0:
                new = '#'
            updated[y].append(new)
    return updated

def printField(field):
    for r in field:
        for s in r:
            print(s, end='')
        print('')
    print('')

field = [[c for c in row] for row in lines]
fieldCopy = copy.deepcopy(field)
last = -1
while last != occupied(field):
    printField(field)
    time.sleep(0.1)
    last = occupied(field)
    field = update(field)

print("First: " + str(occupied(field)))
input()
last = -1
field = fieldCopy
while last != occupied(field):
    printField(field)
    time.sleep(0.1)
    last = occupied(field)
    field = deepUpdate(field)

printField(field)
print("Second: " + str(occupied(field)))
