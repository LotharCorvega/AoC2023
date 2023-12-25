import regex

file = open("input.txt", "r").read()
lines = [line for line in file.split("\n")]

# assuming that brick-line coordinates are given in ascending order:
#   x0,y0,z0~x1,y1,z1 -> x0 <= x1 and y0 <= y1 and z0 <= z1
bricks = []

for line in lines:
    bricks.append(tuple(map(int, regex.match("(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)", line).groups())))

def collideSegment(segment0, segment1):
    s0, e0 = segment0
    s1, e1 = segment1
    
    return s0 <= e1 and s1 <= e0

def collideBricks(brick0, brick1):
    sx0, sy0, sz0, ex0, ey0, ez0 = brick0
    sx1, sy1, sz1, ex1, ey1, ez1 = brick1
    
    return collideSegment((sx0, ex0), (sx1, ex1)) and collideSegment((sy0, ey0), (sy1, ey1)) and collideSegment((sz0, ez0), (sz1, ez1))

def setBrickZ(brick, z):
    sx, sy, sz, ex, ey, ez = brick
    
    return (sx, sy, z, ex, ey, z + (ez - sz))

def supports(brickBelow, brickAbove):
    return brickBelow[5] + 1 == brickAbove[2] and collideBricks(setBrickZ(brickBelow, brickBelow[2] + 1), brickAbove)

def isStable(brick, bricks):
    if brick[2] == 1:
        return True
    
    for b in bricks:
        if supports(b, brick):
            return True
    
    return False

bricks = sorted(bricks, key=lambda tup: tup[2])
n = len(bricks)
heightCap = 1

for i in range(n):
    b = bricks[i]
    b = setBrickZ(b, min(b[2], heightCap))
    
    while True:
        if isStable(b, bricks[:i]):
            break
        
        b = setBrickZ(b, b[2] - 1)
    
    bricks[i] = b
    heightCap = max(heightCap, b[5] + 1)

disintegrate = set(range(n))

for i in range(n):
    S = set()
    
    for j in range(n):
        if i != j and supports(bricks[j], bricks[i]):
            S.add(j)
    
    if len(S) == 1:
        s = S.pop()
        if s in disintegrate:
            disintegrate.remove(s)

for i in range(n):
    isPeak = True
    
    for j in range(n):
        if i != j and supports(bricks[i], bricks[j]):
            isPeak = False
            break
    
    if isPeak:
        disintegrate.add(i)

print(len(disintegrate))