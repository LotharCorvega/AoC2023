file = open("input.txt", "r").read()
steps = file.split(",")

s = 0

for step in steps:
    h = 0
    
    for c in step:
        h += ord(c)
        h = (h * 17) % 256
    
    s += h

print(s)
