import math

file = open("input.txt", "r").read()
lines = file.split("\n")

times = [int(n) for n in lines[0].split()[1:]]
distances = [int(n) for n in lines[1].split()[1:]]

p = 1

for i in range(len(times)):
    t = times[i]
    d = distances[i]
    
    det = math.sqrt(t * t - 4 * d) # term in sqrt could be negative
    
    x0 = (-t + det) / -2
    x1 = (-t - det) / -2
    
    ways = math.ceil(x1 - 1) - math.floor(x0 + 1) + 1
    
    if ways > 0:
        p *= ways

print(p)
