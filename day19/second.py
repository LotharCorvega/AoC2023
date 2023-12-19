import regex

file = open("input.txt", "r").read()
section = [section.split("\n") for section in file.split("\n\n")]

workflow = {}

for line in section[0]:
    name, rules = regex.match("(\w+)\{(\S+)\}", line).groups()
    r = []
    
    for rule in rules.split(","):
        if ":" in rule:
            variable, comperator, value, nextFlow = regex.match("(x|m|a|s)(<|>)(\d+):(\w+)", rule).groups()
            r.append((variable, comperator, int(value), nextFlow))
        else:
            r.append(rule)
    
    workflow[name] = r

def applyConstraint(constraint, interval):
    variable, symbol, value = constraint
    i = "xmas".index(variable)
    l = list(interval)
    
    if symbol == "<":
        vMin, vMax = l[i]
        
        if value > vMin:
            l[i] = (vMin, value - 1)
            return tuple(l)
        else:
            return False
    elif symbol == ">":
        vMin, vMax = l[i]
        
        if value < vMax:
            l[i] = (value + 1, vMax)
            return tuple(l)
        else:
            return False

def applyInvConstraint(constraint, interval):
    variable, symbol, value = constraint
    
    if symbol == "<":
        return applyConstraint((variable, ">", value - 1), interval)
    elif symbol == ">":
        return applyConstraint((variable, "<", value + 1), interval)

acceptingIntervals = []

def process(name, interval):
    if name == "A":
        acceptingIntervals.append(interval)
        return
    elif name == "R":
        return
    
    for rule in workflow[name]:
        if type(rule) == str:
            process(rule, interval)
            break
        
        applied = applyConstraint(rule[:3], interval)
        interval = applyInvConstraint(rule[:3], interval)
        
        if applied:
            process(rule[3], applied)
        
        if not interval:
            break;

process("in", ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))

s = 0

for interval in acceptingIntervals:
    m = 1
    for dimension in interval:
        m *= (dimension[1] - dimension[0] + 1)
    s += m

print(s)