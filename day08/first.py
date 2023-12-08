import regex

file = open("input.txt", "r").read().split("\n\n")

pattern = file[0]
graph = {}

for line in file[1].split("\n"):
    node, left, right = regex.match("(\w+) = \((\w+), (\w+)\)", line).groups()
    
    graph[node] = (left, right)

step = 0
node = "AAA"

while node != "ZZZ":
    direction = pattern[step % len(pattern)]
    node = graph[node][0] if direction == "L" else graph[node][1]
    step += 1

print(step)