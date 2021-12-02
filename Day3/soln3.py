import operator
import functools

inFile = open('../inputs/Day3.txt')
lines = inFile.readlines()

xStrides = [1, 3, 5, 7, 1]
yStrides = [1, 1, 1, 1, 2]
width = len(lines[0])

free = '.'
tree = '#'

outputs = []

for x in range(0, len(xStrides)):
    counter = 0
    tally = 0
    for i in range(0, len(lines), yStrides[x]):
        l = lines[i]
        if l[counter] == tree:
            tally += 1
        if (x == 0):
            print(l[counter])
            print(counter)
        counter += xStrides[x]
        counter = counter % (width - 1)
    outputs.append(tally)

print("First: " + str(outputs[1]))
print("Second: " + str(functools.reduce(operator.mul, outputs, 1)))
