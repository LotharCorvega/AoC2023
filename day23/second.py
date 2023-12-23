file = open("input.txt", "r").read()
grid = [list(line) for line in file.split("\n")]

width = len(grid[0])
height = len(grid)

offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
start = (0, 1)
end = (height - 1, width - 2)

def isCrossing(v):
    y, x = v
    
    if x < 1 or x >= width - 1 or y < 1 or y >= height - 1:
        return v == start or v == end
    elif grid[y][x] == "#":
        return False
    
    count = 0
    
    for offset in offsets:
        if grid[y + offset[0]][x + offset[1]] != "#":
            count += 1
    
    return count > 2

G = {}

for y0 in range(0, height):
    for x0 in range(0, width):
        p = (y0, x0)
        
        if isCrossing(p):
            G[p] = set()
            S = [p]
            dist = {p:0}
            
            while len(S) > 0:
                v = S.pop()
                
                for offset in offsets:
                    u = (v[0] + offset[0], v[1] + offset[1])
                    y, x = u
                    
                    if x < 0 or x >= width or y < 0 or y >= height or grid[y][x] == "#" or u in dist:
                        continue
                    
                    dist[u] = dist[v] + 1
                    
                    if isCrossing(u):
                        G[p].add((u, dist[u]))
                    else:
                        S.append(u)

maxLength = 0

def dfs(v, d, visited):
    global maxLength
    
    if v == end:
        maxLength = max(maxLength, d)
        return
    
    for g in G[v]:
        u, dd = g
        
        if u in visited:
            continue
        
        newVisited = visited.copy()
        newVisited.add(v)
        
        dfs(u, d + dd, newVisited)

dfs(start, 0, set())
print(maxLength)