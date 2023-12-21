file = open("input.txt", "r").read()
grid = [line for line in file.split("\n")]

# assuming:
# - grid is square
# - gird sidelength is odd
# - start is in the center

size = len(grid)
half = size // 2

offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]

EVEN = set()
ODD = set()

new = {(half, half)}
steps = 0
maxSteps = 64

while steps <= maxSteps:
    nextNew = set()
    
    for v in new:
        for offset in offsets:
            u = (v[0] + offset[0], v[1] + offset[1])
            x, y = u
            
            if x >= 0 and x < size and y >= 0 and y < size and not grid[y][x] == "#":
                nextNew.add(u)
    
    if steps % 2 == 0:
        EVEN.update(new)
    else:
        ODD.update(new)
    
    new = nextNew
    steps += 1

print(len(EVEN) if maxSteps % 2 == 0 else len(ODD))