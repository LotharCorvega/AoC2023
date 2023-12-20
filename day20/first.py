from collections import deque

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
low = 0
high = 0

for i in range(1000):
    pulses.append(("button", "broadcaster", False))
    
    while len(pulses) > 0:
        sender, tag, value = pulses.popleft()
        low += not value
        high += value
        
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
                
                for outputModule in module[1]:
                    pulses.append((tag, outputModule, send))

print(low * high)