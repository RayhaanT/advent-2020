inFile = open('../inputs/Day2.txt', 'r')
inputs = inFile.readlines()

def isValidFirst(string, char, low, high):
    tally = 0
    for x in string:
        if x == char:
            tally += 1
    if low <= tally and tally <= high:
        return True
    return False

def isValidSecond(string, char, ind1, ind2):
    tally = 0
    if string[ind1 - 1] == char:
        tally += 1
    if string[ind2 - 1] == char:
        tally += 1
    return (tally == 1)

firstTally = 0
secondTally = 0
for line in inputs:
    arr = line.split()
    string = arr[2]
    char = arr[1][0] # Take only first element, 2nd is colon
    nums = arr[0].split('-')
    low = int(nums[0])
    high = int(nums[1])
    if isValidFirst(string, char, low, high):
        firstTally += 1
    if isValidSecond(string, char, low, high):
        secondTally += 1

print("First: " + str(firstTally))
print("Second: " + str(secondTally))
