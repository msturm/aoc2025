#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '3.in'
#file1 = '3.test'

def find_highest(r, start, remain):
    if remain == 0:
        return 0
    max_v = 0
    pos = 0
    for a in range(start, len(v)-remain+1):
        if int(r[a]) > max_v:
            pos = a
            max_v = int(r[a])
    print(max_v)
    return (max_v*(10**(remain-1))) + find_highest(r, pos+1, remain - 1)

ans1 = 0
ans2 = 0
input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
    x = find_highest(v, 0, 2)
    print(v, x)
    ans1 += x
    x = find_highest(v, 0, 12)
    print(v, x)
    ans2 += x
#    max_v = 0
#    for a in range(0, len(v)):
#        for b in range(a+1, len(v)):
#            if int(v[a] + v[b]) > max_v:
#                max_v = int(v[a] + v[b])
#    print(v, max_v)

print('ans1', ans1)
print('ans2', ans2)

