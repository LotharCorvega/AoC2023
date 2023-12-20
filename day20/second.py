from collections import deque
from math import lcm

file = open("input.txt", "r").read()
lines = file.split("\n")

modules = {}

for line in lines:
    tag, outputs = line.split(" -> ")
    outputs = outputs.split(", ")
    
    if tag == "broadcaster":
        modules[tag] = ([], outputs, "broadcast")
    elif tag[0] == "%":
        modules[tag[1:]] = ([], outputs, "flip-flop")
    elif tag[0] == "&":
        modules[tag[1:]] = ([], outputs, "conjunction")

for tag in list(modules):
    for outputModule in modules[tag][1]:
        if outputModule in modules:
            modules[outputModule][0].append(tag)
        else:
            modules[outputModule] = ([tag], [], "receive")

state = {}

for tag in modules:
    match modules[tag][2]:
        case "broadcast":
            continue
        case "receive":
            continue
        case "flip-flop":
            state[tag] = False
        case "conjunction":
            d = {}
            for inp in modules[tag][0]:
                d[inp] = False
            state[tag] = d

pulses = deque()
cycles = {key : -1 for key in modules["gq"][0]} # gq -> rx (not general)
i = 0

while True:
    if min(cycles.values()) > 0:
        break
    
    pulses.append(("button", "broadcaster", False))
    i += 1
    
    while len(pulses) > 0:
        sender, tag, value = pulses.popleft()
        
        module = modules[tag]
        match module[2]:
            case "broadcast":
                for outputModule in module[1]:
                    pulses.append((tag, outputModule, value))
            case "receive":
                continue
            case "flip-flop":
                if value:
                    continue
                
                state[tag] = not state[tag]
                
                for outputModule in module[1]:
                    pulses.append((tag, outputModule, state[tag]))
            case "conjunction":
                state[tag][sender] = value
                send = False
                
                for inputModule in state[tag]:
                    if not state[tag][inputModule]:
                        send = True
                        break
                
                if send == True and tag in cycles and cycles[tag] == -1:
                    cycles[tag] = i
                
                for outputModule in module[1]:
                    pulses.append((tag, outputModule, send))

print(lcm(*cycles.values()))