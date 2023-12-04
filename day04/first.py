file = open("input.txt", "r").read()
lines = file.split("\n")

s = 0

for line in lines:
    split = line.split(":")[1].split("|")
    
    winningNumbers = [int(n) for n in split[0].split()]
    numbers = [int(n) for n in split[1].split()]
    
    p = 0
    
    for number in numbers:
        if number in winningNumbers:
            p = 1 if p == 0 else p * 2
    
    s += p

print(s)