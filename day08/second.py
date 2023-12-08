import regex
import math

file = open("input.txt", "r").read().split("\n\n")

pattern = file[0]
graph = {}

for line in file[1].split("\n"):
    node, left, right = regex.match("(\w+) = \((\w+), (\w+)\)", line).groups()
    
    graph[node] = (left, right)

cycleLengths = []

for node in graph:
    if node[2] == "A":
        step = 0
        
        while node[2] != "Z":
            direction = pattern[step % len(pattern)]
            node = graph[node][0] if direction == "L" else graph[node][1]
            step += 1
        
        cycleLengths.append(step)

print(math.lcm(*cycleLengths))