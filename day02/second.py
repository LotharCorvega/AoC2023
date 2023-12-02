import regex

file = open("input.txt", "r").read()
lines = file.split("\n")

def parseSubset(subset):
    stones = subset.split(",")
    colors = [0, 0, 0]
    
    for stone in stones:
        if "red" in stone:
            colors[0] = int(regex.findall("\d+", stone)[0])
        elif "green" in stone:
            colors[1] = int(regex.findall("\d+", stone)[0])
        elif "blue" in stone:
            colors[2] = int(regex.findall("\d+", stone)[0])
        else:
            print("error parsing: " + subset)
    
    return tuple(colors)

s = 0

for line in lines:
    parse = line.split(":")
    
    gameId = int(regex.findall("\d+", parse[0])[0])
    subsets = parse[1].split(";")
    
    maxColors = [0, 0, 0]
    
    for subset in subsets:
        colors = parseSubset(subset)
        
        if colors[0] > maxColors[0]:
            maxColors[0] = colors[0]
        if colors[1] > maxColors[1]:
            maxColors[1] = colors[1]
        if colors[2] > maxColors[2]:
            maxColors[2] = colors[2]
    
    s += maxColors[0] * maxColors[1] * maxColors[2]

print(s)