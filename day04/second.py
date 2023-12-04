file = open("input.txt", "r").read()
lines = file.split("\n")

copies = [1] * len(lines)

for i in range(len(lines)):
    split = lines[i].split(":")[1].split("|")
    
    winningNumbers = [int(n) for n in split[0].split()]
    numbers = [int(n) for n in split[1].split()]
    
    p = 0
    
    for number in numbers:
        if number in winningNumbers:
            p += 1
    
    for j in range(i + 1, i + p + 1):
        copies[j] += copies[i]

print(sum(copies))