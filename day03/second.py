file = open("input.txt", "r").read()
grid = [line for line in file.split("\n")]

def getGears(line, start, end):
    gears = []
    for i in range(max(0, line - 1), min(len(grid), line + 2)):
        for j in range(max(0, start - 1), min(len(grid[line]), end + 1)):
            if not (i == line and j in range(start, end)) and grid[i][j] == "*":
                gears.append((i, j))
    return gears

readingNum = False
start = 0
partNumbers = {}

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not readingNum and grid[i][j].isnumeric():
            start = j
            readingNum = True
        
        if readingNum and not grid[i][j].isnumeric():
            for gear in getGears(i, start, j):
                if not gear in partNumbers:
                    partNumbers[gear] = [int(grid[i][start:j])]
                else:
                    partNumbers[gear].append(int(grid[i][start:j]))
            readingNum = False
    
    if readingNum:
        for gear in getGears(i, start, j):
            if not gear in partNumbers:
                partNumbers[gear] = [int(grid[i][start:])]
            else:
                partNumbers[gear].append(int(grid[i][start:]))
        readingNum = False

s = 0

for gear in partNumbers:
    if len(partNumbers[gear]) == 2:
        s += partNumbers[gear][0] * partNumbers[gear][1]

print(s)
