file = open("input.txt", "r").read()
steps = file.split(",")

def hashLabel(s):
    h = 0
    
    for c in s:
        h += ord(c)
        h = (h * 17) % 256
    
    return h

boxes = [[] for i in range(256)]

for step in steps:
    if "=" in step:
        label = step[:-2]
        h = hashLabel(label)
        
        boxList = boxes[h]
        replaced = False
        
        for i in range(len(boxList)):
            if label == boxList[i][:-2]:
                boxList[i] = step
                replaced = True
                break
        
        if not replaced:
            boxList.append(step)
        
    elif "-" in step:
        label = step[:-1]
        h = hashLabel(label)
        
        boxList = boxes[h]
        
        for i in range(len(boxList)):
            if label == boxList[i][:-2]:
                boxList.pop(i)
                break
    else:
        print("unknown operation")

s = 0

for i in range(256):
    for j in range(len(boxes[i])):
        s += (i + 1) * (j + 1) * int(boxes[i][j][-1])

print(s)