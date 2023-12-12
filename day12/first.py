file = open("input.txt", "r").read()
lines = file.split("\n")

records = []

for line in lines:
    split = line.split()
    groups = tuple([int(n) for n in split[1].split(",")])
    
    records.append((split[0], groups))

def fits(string, index, length):
    if index < 0 or index + length > len(string):
        return False
    
    if index > 0 and string[index - 1] == "#":
        return False
    
    if index + length < len(string) and string[index + length] == "#":
        return False
    
    for j in range(index, index + length):
        if string[j] == ".":
            return False
    
    return True

MEM = {}

def ways(record):
    if record in MEM:
        return MEM[record]
    
    s = record[0]
    l = list(record[1])
    w = 0
    
    if len(l) == 0:
        return not "#" in s
    
    for i in range(len(s)):
        if fits(s, i, l[0]):
            r = (s[i + l[0] + 1:], tuple(l[1:]))
            val = ways(r)
            
            MEM[r] = val
            w += val
        if s[i] == "#":
            break
    
    return w

s = 0

for record in records:
    MEM.clear()
    s += ways(record)

print(s)