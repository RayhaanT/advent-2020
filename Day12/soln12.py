import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day12.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

vert = 0
horz = 0
direction = 1   # 0 mod 4 = North
                # 1 mod 4 = East
                # 2 mod 4 = South
                # 3 mod 4 = West

for l in lines:
    op = l[0]
    delta = int(l[1:])
    if op == 'N':
        vert += delta
    if op == 'S':
        vert -= delta
    if op == 'E':
        horz += delta
    if op == 'W':
        horz -= delta
    if op == 'R':
        direction += delta/90
    if op == 'L':
        direction -= delta/90
    if op == 'F':
        if direction % 2 == 0:
            vert += (1 if direction % 4 == 0 else -1) * delta
        if direction % 2 == 1:
            horz += (1 if direction % 4 == 1 else -1) * delta

print("First: " + str(abs(vert) + abs(horz)))

vert = 0
horz = 0
direction = 1
wayY = 1
wayX = 10

for l in lines:
    op = l[0]
    delta = int(l[1:])
    dy = wayY - vert
    dx = wayX - horz
    if op == 'N':
        wayY += delta
    if op == 'S':
        wayY -= delta
    if op == 'E':
        wayX += delta
    if op == 'W':
        wayX -= delta
    if op == 'R':
        for i in range(0, int(delta/90)):
            odx = dx
            dx = dy
            dy = -odx
            wayY = vert + dy
            wayX = horz + dx
    if op == 'L':
        for i in range(0, int(delta/90)):
            odx = dx
            dx = -dy
            dy = odx
            wayY = vert + dy
            wayX = horz + dx
    if op == 'F':
        vert += dy * delta
        horz += dx * delta
        wayY = vert + dy
        wayX = horz + dx

print("Second: " + str(abs(vert) + abs(horz)))
