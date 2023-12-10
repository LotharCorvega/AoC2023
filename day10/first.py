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

print(maxDist)