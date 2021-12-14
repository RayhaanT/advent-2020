import os
dirname = os.path.dirname(__file__)
inputPath = os.path.join(dirname, '../inputs/Day8.txt')

rawLines = []
with open(inputPath) as file:
    rawLines = file.readlines()
lines = [l.strip() for l in rawLines]

instructions = []
for l in lines:
    arr = l.split(' ')
    instructions.append([arr[0], int(arr[1])])

def loops(instructions):
    accumulator = 0
    instructionCounter = 0
    run = []
    while instructionCounter not in run and instructionCounter < len(instructions):
        op = instructions[instructionCounter]
        run.append(instructionCounter)
        instructionCounter += 1
        if op[0] == 'nop':
            continue
        if op[0] == 'acc':
            accumulator += op[1]
        if op[0] == 'jmp':
            instructionCounter += op[1] - 1
    return (accumulator, instructionCounter)


print("First: " + str(loops(instructions)[0]))

for i in range(0, len(instructions)):
    if instructions[i][0] == 'nop':
        instructions[i][0] = 'jmp'
        result = loops(instructions)
        if result[1] == len(instructions):
            print("Second: " + str(result[0]))
            break
        instructions[i][0] = 'nop'
    if instructions[i][0] == 'jmp':
        instructions[i][0] = 'nop'
        result = loops(instructions)
        if result[1] == len(instructions):
            print("Second: " + str(result[0]))
            break
        instructions[i][0] = 'jmp'
