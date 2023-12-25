import regex

file = open("input.txt", "r").read()
lines = [line for line in file.split("\n")]

hailstones = []

for line in lines:
    hailstones.append(tuple(map(int, regex.match("(-?\d+),\s+(-?\d+),\s+(-?\d+)\s+\@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)", line).groups())))

MIN = 200000000000000
MAX = 400000000000000

def getTimes(p, v):
    if v == 0:
        return (p, p) if (p >= MIN and p <= MAX) else False
    
    tMin = (MIN - p) / v
    tMax = (MAX - p) / v
    
    if p < MIN:
        if v < 0:
            return False
        else:
            return (tMin, tMax)
    elif p > MAX:
        if v > 0:
            return False
        else:
            return (tMax, tMin)
    else:
        if v > 0:
            return (0, tMax)
        else:
            return (0, tMin)

def getSegment(hailstone):
    px, py, pz, vx, vy, vz = hailstone
    
    tx = getTimes(px, vx)
    ty = getTimes(py, vy)
    
    if not tx or not ty:
        return False
    
    t0 = max(tx[0], ty[0])
    t1 = min(tx[1], ty[1])
    
    if t1 < t0:
        return False
    
    sx = (px + t0 * vx, px + t1 * vx)
    sy = (py + t0 * vy, py + t1 * vy)
    
    return ((sx[0], sy[0]), (sx[1], sy[1]))

def ccw(A, B, C): # counterclockwise
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def intersect(hailstone0, hailstone1):
    s0 = getSegment(hailstone0)
    s1 = getSegment(hailstone1)
    
    if not s0 or not s1:
        return False
    
    A, B = getSegment(hailstone0)
    C, D = getSegment(hailstone1)
    
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

count = 0

for i in range(len(hailstones)):
    for j in range(i):
        if intersect(hailstones[i], hailstones[j]):
            count += 1

print(count)