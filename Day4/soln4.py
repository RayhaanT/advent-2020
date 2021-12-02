inFile = open('../inputs/Day4.txt')
lines = inFile.readlines()

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isValidFirst(passport):
    eSheet = required.copy()
    pairs = passport.split()
    for p in pairs:
        key = p.split(':')[0]
        try:
            eSheet.remove(key)
        except ValueError:
            continue
    return len(eSheet) == 0

def byrVerify(v):
    v = int(v)
    return (1920 <= v and v <= 2002)

def iyrVerify(v):
    v = int(v)
    return (2010 <= v and v <= 2020)

def eyrVerify(v):
    v = int(v)
    return (2020 <= v and v <= 2030)

def hgtVerify(v):
    if "in" in v:
        v = int(v[:-2])
        return (59 <= v and v <= 76)
    if "cm" in v:
        v = int(v[:-2])
        return (150 <= v and v <= 193)
    return False

def hclVerify(v):
    if(v[0] != "#"):
        return False
    v = v[1:]
    if (len(v) != 6):
        return False
    for c in v:
        if not (c.isdigit() or c.islower()):
            return False
    return True

def eclVerify(v):
    return v in eyeColors

def pidVerify(v):
    if (len(v) != 9):
        return False
    return v.isdigit()

# Ditched in favor of mega sus eval method
verificationTable = {
    'byr' : byrVerify,
    'iyr' : iyrVerify,
    'eyr' : eyrVerify,
    'hgt' : hgtVerify,
    'hcl' : hclVerify,
    'ecl' : eclVerify,
    'pid' : pidVerify
}

def isValidSecond(passport):
    pairs = passport.split()
    for p in pairs:
        block = p.split(':')
        key = block[0]
        value = block[1]
        passed = False
        if key == "cid":
            continue
        func = key + "Verify"
        passed = eval(func + "(value)")
        # passed = verificationTable[key](value)
        if not passed:
            return False
    return True

running = []
tally = 0
secondTally = 0

for l in lines:
    if len(l) == 1:
        if len(running) == 0:
            continue
        passport = running[0][:-1] # Slice to get rid of \n
        for r in range(1, len(running)):
            passport += " " + running[r][:-1]
        if isValidFirst(passport):
            tally += 1
            if isValidSecond(passport):
                secondTally += 1

        running = []
    else:
        running.append(l)

if len(running) != 0:
  passport = running[0][:-1]
  for r in range(1, len(running)):
    passport += " " + running[r][:-1]
  if isValidFirst(passport):
    tally += 1

print("First: " + str(tally))
print("Second: " + str(secondTally))
