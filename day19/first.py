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

def process(p, name):
    while True:
        if name == "A":
            return True
        if name == "R":
            return False
        
        for rule in workflow[name]:
            if type(rule) == str:
                name = rule
                break
            elif (rule[1] == "<" and p[rule[0]] < rule[2]) or (rule[1] == ">" and p[rule[0]] > rule[2]):
                name = rule[3]
                break

ss = 0

for part in section[1]:
    x, m, a, s = map(int, regex.match("\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", part).groups())
    p = {"x":x, "m":m, "a":a, "s":s}
    
    if process(p, "in"):
        ss += x + m + a + s

print(ss)