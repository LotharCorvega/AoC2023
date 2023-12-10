from collections import deque

file = open("input.txt", "r").read()
grid = file.split("\n")

height = len(grid)
width = len(grid[0])

dist = [[-1] * width for i in range(height)]
start = (-1, -1)

for i in range(height):
    if "S" in grid[i]:
        start = (i, grid[i].index("S"))
        break;

offsets = {
    "S": [(-1,  0, "|7F"), ( 1,  0, "|LJ"), ( 0, -1, "-LF"), ( 0,  1, "-J7")],
    "|": [(-1,  0, "|7F"), ( 1,  0, "|LJ")],
    "-": [( 0, -1, "-LF"), ( 0,  1, "-J7")],
    "L": [(-1,  0, "|7F"), ( 0,  1, "-J7")],
    "J": [(-1,  0, "|7F"), ( 0, -1, "-LF")],
    "7": [( 1,  0, "|LJ"), ( 0, -1, "-LF")],
    "F": [( 1,  0, "|LJ"), ( 0,  1, "-J7")]
}

Q = deque()
Q.append(start)

dist[start[0]][start[1]] = 0
maxDist = 0

while len(Q) > 0:
    y, x = Q.popleft()
    v = grid[y][x]
    d = dist[y][x]
    
    for offset in offsets[v]:
        n = (y + offset[0], x + offset[1])
        
        if dist[n[0]][n[1]] == -1 and grid[n[0]][n[1]] in offset[2]:
            dist[n[0]][n[1]] = d + 1
            maxDist = max(maxDist, d + 1)
            Q.append(n)

grid3 = [[0] * (width * 3) for i in range(height * 3)]

def setBlock(x, y, symbol):
    x3 = x * 3
    y3 = y * 3
    
    match symbol:
        case "S":
            grid3[y3 + 0][x3:x3 + 3] = [0, 1, 0]
            grid3[y3 + 1][x3:x3 + 3] = [1, 1, 1]
            grid3[y3 + 2][x3:x3 + 3] = [0, 1, 0]
        case "|":
            grid3[y3 + 0][x3:x3 + 3] = [0, 1, 0]
            grid3[y3 + 1][x3:x3 + 3] = [0, 1, 0]
            grid3[y3 + 2][x3:x3 + 3] = [0, 1, 0]
        case "-":
            grid3[y3 + 0][x3:x3 + 3] = [0, 0, 0]
            grid3[y3 + 1][x3:x3 + 3] = [1, 1, 1]
            grid3[y3 + 2][x3:x3 + 3] = [0, 0, 0]
        case "L":
            grid3[y3 + 0][x3:x3 + 3] = [0, 1, 0]
            grid3[y3 + 1][x3:x3 + 3] = [0, 1, 1]
            grid3[y3 + 2][x3:x3 + 3] = [0, 0, 0]
        case "J":
            grid3[y3 + 0][x3:x3 + 3] = [0, 1, 0]
            grid3[y3 + 1][x3:x3 + 3] = [1, 1, 0]
            grid3[y3 + 2][x3:x3 + 3] = [0, 0, 0]
        case "7":
            grid3[y3 + 0][x3:x3 + 3] = [0, 0, 0]
            grid3[y3 + 1][x3:x3 + 3] = [1, 1, 0]
            grid3[y3 + 2][x3:x3 + 3] = [0, 1, 0]
        case "F":
            grid3[y3 + 0][x3:x3 + 3] = [0, 0, 0]
            grid3[y3 + 1][x3:x3 + 3] = [0, 1, 1]
            grid3[y3 + 2][x3:x3 + 3] = [0, 1, 0]

for y in range(height):
    for x in range (width):
        if dist[y][x] != -1:
            setBlock(x, y, grid[y][x])

offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]

Q.append((0, 0))
grid3[0][0] = 2

while len(Q) > 0:
    y, x = Q.popleft()
    
    for offset in offsets:
        n = (y + offset[0], x + offset[1])
        
        if n[0] < 0 or n[0] >= (height * 3) or n[1] < 0 or n[1] >= (width * 3):
            continue
        
        if grid3[n[0]][n[1]] == 0:
            grid3[n[0]][n[1]] = 2
            Q.append(n)

def checkBlock(x, y):
    x3 = x * 3
    y3 = y * 3
    
    if grid3[y3 + 0][x3:x3 + 3] != [0, 0, 0] or grid3[y3 + 1][x3:x3 + 3] != [0, 0, 0] or grid3[y3 + 2][x3:x3 + 3] != [0, 0, 0]:
        return False
    
    return True

c = 0

for y in range(height):
    for x in range(width):
        if checkBlock(x, y):
            c += 1

print(c)