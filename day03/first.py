file = open("input.txt", "r").read()
grid = [line for line in file.split("\n")]

def checkForSymbols(line, start, end):
    for i in range(max(0, line - 1), min(len(grid), line + 2)):
        for j in range(max(0, start - 1), min(len(grid[line]), end + 1)):
            if not (i == line and j in range(start, end)) and grid[i][j] != "." and not grid[i][j].isnumeric():
                return True
    return False

readingNum = False
start = 0
s = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not readingNum and grid[i][j].isnumeric():
            start = j
            readingNum = True
        
        if readingNum and not grid[i][j].isnumeric():
            if checkForSymbols(i, start, j):
                s += int(grid[i][start:j])
            readingNum = False
    
    if readingNum:
        if checkForSymbols(i, start, len(grid[i])):
            s += int(grid[i][start:])
        readingNum = False

print(s)
