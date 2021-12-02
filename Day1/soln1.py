inFile = open('../inputs/Day1.txt', 'r')
inputs = inFile.readlines()
inputs = [int(x) for x in inputs]
done = False

for x in inputs:
    if done:
        break
    for y in inputs:
        if x + y == 2020:
            print("First: " + str(x*y))
            done = True
            break

done = False
for x in inputs:
    if done:
        break
    for y in inputs:
        if done:
            break
        for z in inputs:
            if x + y + z == 2020:
                print("Second: " + str(x * y * z))
                done = True
                break
