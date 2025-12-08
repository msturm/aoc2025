#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque
import math

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

def is_invalid(x):
    x = str(x)
    return x[len(x)//2:] == x[:len(x)//2]

def is_invalid2(x):
    x = str(x)
    print('checking', x)
    for l in range(2, len(x)+1):
        if len(x)%l == 0:
            i = 0
            ok = True
            while i < len(x):
                if x[i:i+len(x)//l] != x[:len(x)//l]:
                    ok = False
                i += len(x)//l
            if ok:
                return True
                
        
    return False

file1 = '2.in'
#file1 = '2.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
ans1 = 0
ans2 = 0
for v in input[0].split(','):
    s, e = v.split('-')
    
    for i in range(int(s), int(e)+1):
        if is_invalid(i):
            ans1 += int(str(i))
        if is_invalid2(i):
            ans2 += int(str(i))
            
print('ans1', ans1)
print('ans2', ans2)

