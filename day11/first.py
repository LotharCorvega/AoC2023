file = open("input.txt", "r").read()
lines = file.split("\n")

xOffsets = []
yOffset = 0

hasHashtag = False

for y in range(len(lines)):
    if lines[y][0] == "#":
        hasHashtag = True
        break

if hasHashtag:
    xOffsets.append(0)
else:
    xOffsets.append(1)

for x in range(1, len(lines[0])):
    hasHashtag = False
    
    for y in range(len(lines)):
        if lines[y][x] == "#":
            hasHashtag = True
            break
    
    if hasHashtag:
        xOffsets.append(xOffsets[x - 1])
    else:
        xOffsets.append(xOffsets[x - 1] + 1)

galaxies = []

for y in range(len(lines)):
    if not "#" in lines[y]:
        yOffset += 1
        continue
    
    for x in range(len(lines[y])):
        if lines[y][x] == "#":
            galaxies.append((y + yOffset, x + xOffsets[x]))

s = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        s += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print(s)
