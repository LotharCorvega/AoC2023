file = open("input.txt", "r").read()
grid = [list(line) for line in file.split("\n")]

width = len(grid[0])
height = len(grid)

def tiltNorth():
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "O":
                roll = 1
                
                while y - roll >= 0 and grid[y - roll][x] == ".":
                    roll += 1
                
                grid[y][x] = "."
                grid[y - roll + 1][x] = "O"

def tiltSouth():
    for y in reversed(range(height)):
        for x in range(width):
            if grid[y][x] == "O":
                roll = 1
                
                while y + roll < height and grid[y + roll][x] == ".":
                    roll += 1
                
                grid[y][x] = "."
                grid[y + roll - 1][x] = "O"

def tiltWest():
    for x in range(width):
        for y in range(height):
            if grid[y][x] == "O":
                roll = 1
                
                while x - roll >= 0 and grid[y][x - roll] == ".":
                    roll += 1
                
                grid[y][x] = "."
                grid[y][x - roll + 1] = "O"

def tiltEast():
    for x in reversed(range(width)):
        for y in range(height):
            if grid[y][x] == "O":
                roll = 1
                
                while x + roll < width and grid[y][x + roll] == ".":
                    roll += 1
                
                grid[y][x] = "."
                grid[y][x + roll - 1] = "O"

def doCycle():
    tiltNorth()
    tiltWest()
    tiltSouth()
    tiltEast()

def load():
    l = 0
    
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "O":
                l += height - y
    
    return l

states = {}
cycle = 0

while True:
    doCycle()
    
    h = hash("".join(["".join(line) for line in grid]))
    cycle += 1
    
    if h in states:
        cycleLength = cycle - states[h]
        rest = (1000000000 - states[h]) % cycleLength
        
        for i in range(rest):
            doCycle()
        
        print(load())
        exit()
    
    states[h] = cycle