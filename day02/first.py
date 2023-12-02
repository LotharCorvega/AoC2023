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

maxColors = (12, 13, 14)
s = 0

for line in lines:
    parse = line.split(":")
    
    gameId = int(regex.findall("\d+", parse[0])[0])
    subsets = parse[1].split(";")
    
    isPossible = True;
    
    for subset in subsets:
        colors = parseSubset(subset)
        
        if colors[0] > maxColors[0] or colors[1] > maxColors[1] or colors[2] > maxColors[2]:
            isPossible = False;
            break;
    
    if isPossible:
        s += gameId

print(s)