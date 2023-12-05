import regex

file = open("input.txt", "r").read()
blocks = [block for block in file.split("\n\n")]

seeds = [int(n) for n in regex.findall("\d+", blocks[0])]

def parseMap(block):
    lines = block.split("\n")
    kind = regex.match("(\w+)-to-(\w+) map:", lines[0]).groups()
    intervals = []
    
    for line in lines[1:]:
        split = [int(n) for n in line.split()]
        intervals.append((split[0], split[1], split[2]))
    
    return (kind, intervals)

allMap = {}

for m in [parseMap(block) for block in blocks[1:]]:
    allMap[m[0][0]] = m

def transition(state):
    value = state[0]
    kind = state[1]
    
    kindMap = allMap[kind]
    newKind = kindMap[0][1]
    intervals = kindMap[1]
    
    for interval in intervals:
        dest = interval[0]
        sour = interval[1]
        rang = interval[2]
        
        if value >= sour and value < sour + rang:
            newValue = value - sour + dest
            return (newValue, newKind)
    
    return (value, newKind)

m = -1

for seed in seeds:
    state = (seed, "seed")
    
    while state[1] != "location":
        state = transition(state)
    
    if m == -1 or state[0] < m:
        m = state[0]

print(m)