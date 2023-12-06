file = open("input.txt", "r").read()
lines = file.split("\n")

times = [int(n) for n in lines[0].split()[1:]]
distances = [int(n) for n in lines[1].split()[1:]]

p = 1

for i in range(len(times)):
    t = times[i]
    d = distances[i]
    
    ways = 0
    
    for lt in range(0, t):
        if (t - lt) * lt > d:
            ways += 1
    
    if ways > 0:
        p *= ways


print(p)
