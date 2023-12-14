file = open("input.txt", "r").read()
grid = [list(line) for line in file.split("\n")]

width = len(grid[0])
height = len(grid)

s = 0

for y in range(height):
    for x in range(width):
        if grid[y][x] == "O":
            roll = 1
            
            while y - roll >= 0 and grid[y - roll][x] == ".":
                roll += 1
            
            grid[y][x] = "."
            grid[y - roll + 1][x] = "O"
            
            s += height - (y - roll + 1)

print(s)