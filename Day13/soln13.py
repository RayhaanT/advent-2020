import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day13.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

def modInverse(n, m):
    n = n % m
    for a in range(1, m):
        if (a * n) % m == 1:
            return a

timestamp = int(lines[0])

buses = []
counter = 0
for l in lines[1].split(','):
    if l == 'x':
        counter += 1
        continue
    buses.append((int(l), counter))
    counter += 1

delta = -1
busID = 0
for b in buses:
    mod = -timestamp % b[0]
    if mod < delta or delta == -1:
        delta = mod
        busID = b[0]

print("First: " + str(busID * delta))

modBase = 1
for b in buses:
    modBase *= b[0]

soln = 0
for b in buses:
    n = int(modBase/b[0])
    soln += -b[1]*n*modInverse(n,b[0])

print("Second: " + str(soln % modBase))
