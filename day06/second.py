file = open("input.txt", "r").read()
lines = file.split("\n")

t = int(lines[0][10:].replace(" ", ""))
d = int(lines[1][10:].replace(" ", ""))

ways = 0

for lt in range(0, t):
    if (t - lt) * lt > d:
        ways += 1

print(ways)