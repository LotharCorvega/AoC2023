file = open("input.txt", "r").read()
lines = file.split("\n")

def difference(values):
    difference = [0] * (len(values) - 1)
    
    for i in range(len(values) - 1):
        difference[i] = values[i + 1] - values[i]
    
    return difference

s = 0

for line in lines:
    history = [int(n) for n in line.split()]
    
    extrapolation = [history]
    i = 0
    
    while True:
        d = difference(extrapolation[i])
        
        if len(set(d)) > 1:
            extrapolation.append(d)
            i += 1
        else:
            extrapolation.append(d)
            break
    
    extrapolation[-1].append(extrapolation[-1][0])
    j = len(extrapolation) - 2
    
    while j >= 0:
        extrapolation[j].append(extrapolation[j][-1] + extrapolation[j + 1][-1])
        j -= 1
    
    s += extrapolation[0][-1]

print(s)