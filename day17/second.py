file = open("input.txt", "r").read()
grid = [[int(n) for n in list(line)] for line in file.split("\n")]

width = len(grid[0])
height = len(grid)

QV = [(0, 0)] # waiting to move vertically
QH = [(0, 0)] # waiting to move horizontally

distV = {} # moved into vertically
distH = {} # moved into horizontally

for y in range(height):
    for x in range(width):
        v = (y, x)
        
        distV[v] = width * height * 10
        distH[v] = width * height * 10

distV[(0, 0)] = 0
distH[(0, 0)] = 0

def moveVertical():
    while len(QV) > 0:
        v = QV.pop()
        y, x = v
        
        up = 0
        down = 0
        
        for i in range(1, 11):
            if y - i >= 0:
                up += grid[y - i][x]
                if i > 3 and distH[v] + up < distV[(y - i, x)]:
                    distV[(y - i, x)] = distH[v] + up
                    QH.append((y - i, x))
            
            if y + i < height:
                down += grid[y + i][x]
                if i > 3 and distH[v] + down < distV[(y + i, x)]:
                    distV[(y + i, x)] = distH[v] + down
                    QH.append((y + i, x))

def moveHorizontal():
    while len(QH) > 0:
        v = QH.pop()
        y, x = v
        
        left = 0
        right = 0
        
        for i in range(1, 11):
            if x - i >= 0:
                left += grid[y][x - i]
                if i > 3 and distV[v] + left < distH[(y, x - i)]:
                    distH[(y, x - i)] = distV[v] + left
                    QV.append((y, x - i))
            
            if x + i < width:
                right += grid[y][x + i]
                if i > 3 and distV[v] + right < distH[(y, x + i)]:
                    distH[(y, x + i)] = distV[v] + right
                    QV.append((y, x + i))

turn = True

while len(QV) > 0 or len(QH) > 0:
    if turn:
        moveVertical()
    else:
        moveHorizontal()
    turn = not turn

corner = (height - 1, width - 1)
print(min(distV[corner], distH[corner]))