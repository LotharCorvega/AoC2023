file = open("input.txt", "r").read()
lines = file.split("\n")

records = []

for line in lines:
    split = line.split()
    groups = tuple([int(n) for n in split[1].split(",")])
    
    records.append(("?".join([split[0]] * 5), groups * 5))

currentString = ""
currentGroups = []
MEM = {}

def fits(offset, index, length):
    if index < 0 or index + offset + length > len(currentString):
        return False
    
    if index > 0 and currentString[index + offset - 1] == "#":
        return False
    
    if index + offset + length < len(currentString) and currentString[index + offset + length] == "#":
        return False
    
    for j in range(index, index + length):
        if currentString[j + offset] == ".":
            return False
    
    return True

def ways(offset, groupIndex):
    if (offset, groupIndex) in MEM:
        return MEM[(offset, groupIndex)]
    
    w = 0
    
    if groupIndex == len(currentGroups):
        return not "#" in currentString[offset:]
    
    for i in range(len(currentString) - offset):
        if fits(offset, i, currentGroups[groupIndex]):
            t = (offset + i + currentGroups[groupIndex] + 1, groupIndex + 1)
            val = ways(*t)
            
            MEM[t] = val
            w += val
        if currentString[offset + i] == "#":
            break
    
    return w

s = 0

for record in records:
    currentString = record[0]
    currentGroups = record[1]
    
    s += ways(0, 0)
    MEM.clear()

print(s)