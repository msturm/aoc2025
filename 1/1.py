#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '1.in'
#file1 = '2.test'

input = [x.strip() for x in open(file1, 'r').readlines()]

ans1 = 0
ans2 = 0
p = 50
for v in input:
    d = v[0:1]
    a = int(v[1:])
    c = 0
    if d == 'L':
        c = (a+(100-p)) // 100
        if p == 0:
            c -= 1
        #print('absL',p, a, abs((p-a)//100))
        p = (p - a) % 100
    else:
        c = (p + a) // 100
        #print('absR',p, a, abs((p+a)//100))
        p = (p + a) % 100
    ans2 += c
    print(d, a, p, ans2)
    if p == 0:
        ans1 += 1

print("ans1", ans1)
print("ans2", ans2)
    
