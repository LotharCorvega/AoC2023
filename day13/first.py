file = open("input.txt", "r").read()
grids = [grid.split("\n") for grid in file.split("\n\n")]

def hasVerticalMirror(gird, col):
    height = len(grid)
    width = len(grid[0])
    
    for y in range(height):
        for d in range(min(col, width - col - 2) + 1):
            if grid[y][col - d] != grid[y][col + 1 + d]:
                return False
    
    return True

def hasHorizontalMirror(gird, row):
    height = len(grid)
    width = len(grid[0])
    
    for x in range(width):
        for d in range(min(row, height - row - 2) + 1):
            if grid[row - d][x] != grid[row + 1 + d][x]:
                return False
    
    return True

s = 0

for grid in grids:
    height = len(grid)
    width = len(grid[0])
    
    for i in range(max(width, height) - 1):
        if i < width - 1 and hasVerticalMirror(grid, i):
            s += i + 1
            break
        if i < height - 1 and hasHorizontalMirror(grid, i):
            s += (i + 1) * 100
            break

print(s)