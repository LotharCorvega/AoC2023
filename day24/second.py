import regex
from z3 import *

file = open("input.txt", "r").read()
lines = [line for line in file.split("\n")]

S = Solver() # feels like cheating
spx, spy, spz, svx, svy, svz = Reals("spx spy spz svx svy svz")

i = 0
for line in lines:
    px, py, pz, vx, vy, vz = map(int, regex.match("(-?\d+),\s+(-?\d+),\s+(-?\d+)\s+\@\s+(-?\d+),\s+(-?\d+),\s+(-?\d+)", line).groups())
    ti = Real(f"t{i}")
    
    S.add(spx + ti * svx == px + ti * vx)
    S.add(spy + ti * svy == py + ti * vy)
    S.add(spz + ti * svz == pz + ti * vz)
    
    i += 1

if S.check():
    m = S.model()
    print(m[spx].as_long() + m[spy].as_long() + m[spz].as_long())
else:
    print("not solution found")