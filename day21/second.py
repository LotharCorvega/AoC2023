file = open("input.txt", "r").read()
grid = [line for line in file.split("\n")]

# assuming:
# - grid is square
# - gird sidelength is odd
# - start is in the center
# - steps = n * size + half (n is a natural number)
# - half is an odd number

size = len(grid)
half = size // 2

offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def calcPlots(start, maxSteps):
    EVEN = set()
    ODD = set()
    
    new = {start}
    steps = 0
    
    while steps <= maxSteps:
        nextNew = set()
        
        for v in new:
            for offset in offsets:
                u = (v[0] + offset[0], v[1] + offset[1])
                x, y = u
                
                if x >= 0 and x < size and y >= 0 and y < size and not grid[y][x] == "#":
                    if steps % 2 == 0 and u not in ODD:
                        nextNew.add(u)
                    elif u not in EVEN:
                        nextNew.add(u)
        
        if steps % 2 == 0:
            EVEN.update(new)
        else:
            ODD.update(new)
        
        new = nextNew
        steps += 1
    
    return len(EVEN) if maxSteps % 2 == 0 else len(ODD)

plotsFullOdd = calcPlots((half, half), size)
plotsFullEven = calcPlots((half, half), size + 1)

plotsS = calcPlots((half, 0), size - 1)
plotsN = calcPlots((half, size - 1), size - 1)
plotsE = calcPlots((0, half), size - 1)
plotsW = calcPlots((size - 1, half), size - 1)

rocksSE_small = calcPlots((0, 0), half - 1)
rocksNE_small = calcPlots((0, size - 1), half - 1)
rocksSW_small = calcPlots((size - 1, 0), half - 1)
rocksNW_small = calcPlots((size - 1, size - 1), half - 1)

rocksSE_large = calcPlots((0, 0), size + half - 1)
rocksNE_large = calcPlots((0, size - 1), size + half - 1)
rocksSW_large = calcPlots((size - 1, 0), size + half - 1)
rocksNW_large = calcPlots((size - 1, size - 1), size + half - 1)

steps = 26501365
wraps = (steps - half) // size
plots = 0

plots += plotsS + plotsN + plotsE + plotsW
plots += (wraps - 0)**2 * plotsFullEven
plots += (wraps - 1)**2 * plotsFullOdd
plots += (wraps - 0) * (rocksSE_small + rocksNE_small + rocksSW_small + rocksNW_small)
plots += (wraps - 1) * (rocksSE_large + rocksNE_large + rocksSW_large + rocksNW_large)

print(plots)