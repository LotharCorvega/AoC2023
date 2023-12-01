import regex

file = open("input.txt", "r").read()
items = [line for line in file.split("\n")]

value = 0

for line in items:
    matches = regex.findall("\d", line)
    value += int(matches[0] + matches[-1])

print(value)