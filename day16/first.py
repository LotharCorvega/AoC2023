from collections import deque

file = open("input.txt", "r").read()
grid = file.split("\n")

width = len(grid[0])
height = len(grid)

energized = [[0] * width for y in range(height)]
states = set()

Q = deque()
Q.append(((-1, 0), (1, 0)))

while len(Q) > 0:
    state = Q.popleft()
    
    if state in states:
        continue
    states.add(state)
    
    pos, direction = state
    newPos = (pos[0] + direction[0], pos[1] + direction[1])
    
    if newPos[0] < 0 or newPos[0] >= width or newPos[1] < 0 or newPos[1] >= height:
        continue
    
    energized[newPos[1]][newPos[0]] = 1
    c = grid[newPos[1]][newPos[0]]
    
    if c == ".":
        Q.append((newPos, direction))
    elif c == "|":
        if direction == (-1, 0) or direction == (1, 0):
            Q.append((newPos, (0, -1)))
            Q.append((newPos, (0, 1)))
        else:
            Q.append((newPos, direction))
    elif c == "-":
        if direction == (0, -1) or direction == (0, 1):
            Q.append((newPos, (-1, 0)))
            Q.append((newPos, (1, 0)))
        else:
            Q.append((newPos, direction))
    elif c == "/":
        if direction == (0, -1):
            Q.append((newPos, (1, 0)))
        elif direction == (0, 1):
            Q.append((newPos, (-1, 0)))
        elif direction == (-1, 0):
            Q.append((newPos, (0, 1)))
        elif direction == (1, 0):
            Q.append((newPos, (0, -1)))
    elif c == "\\":
        if direction == (0, -1):
            Q.append((newPos, (-1, 0)))
        elif direction == (0, 1):
            Q.append((newPos, (1, 0)))
        elif direction == (-1, 0):
            Q.append((newPos, (0, -1)))
        elif direction == (1, 0):
            Q.append((newPos, (0, 1)))
    else:
        print(f"unknown symbol: {c}")
        exit()

print(sum(map(sum, energized)))