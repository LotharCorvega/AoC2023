import regex

file = open("input.txt", "r").read()
lines = file.split("\n")

points = [(0, 0)]
directions = []
borderLength = 0
n = 0

for line in lines:
    d, l, c = regex.match("(L|R|U|D) (\d+) \(#(\w+)\)", line).groups()
    
    x, y = points[-1]
    l = int(c[:-1], 16)
    d = "RDLU"[int(c[-1])]
    
    match d:
        case "L":
            points.append((x - l, y))
        case "R":
            points.append((x + l, y))
        case "U":
            points.append((x, y - l))
        case "D":
            points.append((x, y + l))
    
    directions.append(d)
    borderLength += l
    n += 1

if points[0] != points[-1]:
    print("no cycle")
    exit()

turnsL = 0
turnsR = 0

for i in range(n):
    match directions[i]:
        case "L":
            if directions[(i + 1) % n] == "U":
                turnsR += 1
            elif directions[(i + 1) % n] == "D":
                turnsL += 1
        case "R":
            if directions[(i + 1) % n] == "U":
                turnsL += 1
            elif directions[(i + 1) % n] == "D":
                turnsR += 1
        case "U":
            if directions[(i + 1) % n] == "L":
                turnsL += 1
            elif directions[(i + 1) % n] == "R":
                turnsR += 1
        case "D":
            if directions[(i + 1) % n] == "L":
                turnsR += 1
            elif directions[(i + 1) % n] == "R":
                turnsL += 1

area = borderLength / 2;

if turnsR == turnsL + 4: # clockwise
    area -= turnsL * 1/4
    area += turnsR * 1/4
elif turnsL == turnsR + 4: # counter clockwise
    area += turnsL * 1/4
    area -= turnsR * 1/4
else:
    print("invalid shape")
    exit()

i = 0

while i < len(points) - 1:
    area += (points[i + 1][0] * (points[i + 2][1] - points[i][1]) + points[i + 1][1] * (points[i][0] - points[i + 2][0])) / 2
    i += 2

print(int(area))