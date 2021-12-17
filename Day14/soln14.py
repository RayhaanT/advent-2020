import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day14.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

def fill(h):
    return h.zfill(36)

def binToDec(b):
    return int(b, 2)

def decToBin(d):
    return bin(int(d))[2:]

def applyMask(num, mask):
    num = fill(num)
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            continue
        num = num[:i] + mask[i] + num[i+1:]
    return binToDec(num)

def applyAddrMask(mask, addr):
    addr = fill(addr)
    for i in range(0, len(mask)):
        if mask[i] != 'X' and addr[i] == '1':
            mask = mask[:i] + '1' + mask[i+1:]
    return mask

def applyMaskFloating(mask):
    if 'X' not in mask:
        return [binToDec(mask)]
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            zeroList = applyMaskFloating(mask[:i] + '0' + mask[i+1:])
            oneList = applyMaskFloating(mask[:i] + '1' + mask[i+1:])
            zeroList.extend(oneList)
            return zeroList
    return []

def writeFloating(num, mask, addr, memory):
    addresses = applyMaskFloating(applyAddrMask(mask, decToBin(addr)))
    for a in addresses:
        memory[a] = num
    return memory

mask = ''
memory = {}
for l in lines:
    split = l.split(' ')
    if split[0] == 'mask':
        mask = split[2]
        continue

    addr = split[0].split('[')[1][:-1]
    memory[addr] = applyMask(decToBin(split[2]), mask)

print("First: " + str(sum(memory.values())))

mask = ''
memory = {}
for l in lines:
    split = l.split(' ')
    if split[0] == 'mask':
        mask = split[2]
        continue

    addr = split[0].split('[')[1][:-1]
    memory = writeFloating(int(split[2]), mask, addr, memory)

print("Second: " + str(sum(memory.values())))
