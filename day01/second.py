import regex

file = open("input.txt", "r").read()
items = [line for line in file.split("\n")]

indexer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
value = 0

for line in items:
    matches = regex.findall("(\d|" + "|".join(indexer[10:]) + ")", line, overlapped=True)
    
    first = indexer.index(matches[0])
    last = indexer.index(matches[-1])
    
    if first >= 10:
        first -= 9
    if last >= 10:
        last -= 9
    
    value += first * 10 + last

print(value)