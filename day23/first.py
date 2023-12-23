file = open("input.txt", "r").read()
grid = [list(line) for line in file.split("\n")]

width = len(grid[0])
height = len(grid)

offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
start = (0, 1)
end = (height - 1, width - 2)

dist = [[-1] * width for y in range(height)]
slopes = set()

def dfs(v, d, visited):
    for offset in offsets:
        u = (v[0] + offset[0], v[1] + offset[1])
        y, x = u
        
        if x < 0 or x >= width or y < 0 or y >= height or grid[y][x] == "#" or u in visited:
            continue
        
        if grid[y][x] == ".":
            newVisited = visited.copy()
            newVisited.add(v)
            
            dist[y][x] = max(dist[y][x], d + 1)
            dfs(u, d + 1, newVisited)
        elif offset == (0, -1) and grid[y][x] == "<":
            dist[y][x] = max(dist[y][x], d + 1)
            slopes.add(u)
        elif offset == (0, 1) and grid[y][x] == ">":
            dist[y][x] = max(dist[y][x], d + 1)
            slopes.add(u)
        elif offset == (-1, 0) and grid[y][x] == "^":
            dist[y][x] = max(dist[y][x], d + 1)
            slopes.add(u)
        elif offset == (1, 0) and grid[y][x] == "v":
            dist[y][x] = max(dist[y][x], d + 1)
            slopes.add(u)

dist[start[0]][start[1]] = 0
dfs(start, 0, set())

while len(slopes) > 0:
    currentSlopes = slopes
    slopes = set()
    
    for slope in currentSlopes:
        y, x = slope
        d = dist[y][x]
        
        if grid[y][x] == "<":
            start = (y, x - 1)
            dist[start[0]][start[1]] = d + 1
            dfs(start, d + 1, {start})
        elif grid[y][x] == ">":
            start = (y, x + 1)
            dist[start[0]][start[1]] = d + 1
            dfs(start, d + 1, {start})
        elif grid[y][x] == "^":
            start = (y - 1, x)
            dist[start[0]][start[1]] = d + 1
            dfs(start, d, {start})
        elif grid[y][x] == "v":
            start = (y + 1, x)
            dist[start[0]][start[1]] = d + 1
            dfs(start, d + 1, {start})

print(dist[end[0]][end[1]])