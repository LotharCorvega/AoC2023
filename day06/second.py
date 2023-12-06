import math

file = open("input.txt", "r").read()
lines = file.split("\n")

t = int(lines[0][10:].replace(" ", ""))
d = int(lines[1][10:].replace(" ", ""))

det = math.sqrt(t * t - 4 * d)

x0 = (-t + det) / -2
x1 = (-t - det) / -2

print(math.ceil(x1 - 1) - math.floor(x0 + 1) + 1)