#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '5.in'
#file1 = '5.test'

ans1 = 0

input = [x.strip() for x in open(file1, 'r').readlines()]
sp = [i for (i, x) in enumerate(input) if len(x)==0][0]
F = [x.split('-') for x in input[0:sp]]
F = [(int(a), int(b)) for a, b in F]
I = [int(x) for x in input[sp+1:]]

for i in I:
    ok = False 
    for fs, fe in F:
        if fs <= i <= fe:
            ok = True
            continue
    if ok:
        ans1 += 1

#print(I, F)
print("ans1", ans1)
ans2 = 0
c = 0
F = sorted(F)
for fs, fe in F:
#    print('s', fs, fe, c, ans2)
    if fs > c:
        c = fs
    if fe >= c:
        ans2 += fe - c + 1
        c = fe + 1
#    print('e', fs, fe, c, ans2)


print('ans2', ans2)

    
