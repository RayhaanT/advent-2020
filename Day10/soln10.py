import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day10.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

voltages = [int(l) for l in lines]
voltages.append(0)
voltages.sort()
voltages.append(voltages[-1] + 3)

ones = 0
threes = 0

for v in range(1, len(voltages)):
    delta = voltages[v] - voltages[v-1]
    if delta == 1:
        ones += 1
    if delta == 3:
        threes += 1

print("First: " + str(ones * threes))

voltagePairs = [[v, 0] for v in voltages]

for v in range(len(voltagePairs) - 1, -1, -1):
    if v >= len(voltagePairs) - 3:
        voltagePairs[v][1] = 1
        continue

    thisVoltage = voltagePairs[v][0]
    paths = voltagePairs[v + 1][1]
    if voltagePairs[v + 2][0] - thisVoltage <= 3:
        paths += voltagePairs[v + 2][1]
    if voltagePairs[v + 3][0] - thisVoltage <= 3:
        paths += voltagePairs[v + 3][1]
    voltagePairs[v][1] = paths

print("Second: " + str(voltagePairs[0][1]))
