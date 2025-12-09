#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '6.in'
#file1 = '6.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
raw_input = open(file1, 'r').readlines()
G = []
O = []
for v in input:
    G.append([x for x in re.split(r" +", v)])
O = G.pop()

ans1 = 0
R = len(G)
C = len(G[0])
for c in range(0, C):
    v = 0 if O[c] == '+' else 1 
    for r in range(0, R):
        if O[c] == '+':
            v += int(G[r][c])
        elif O[c] == '*':
            v *= int(G[r][c])
#        print(int(G[r][c]), v)
    ans1+=v           
print('ans1', ans1)
            
input = raw_input
R = len(input)
C = max([len(x) for x in input]) - 1
G = []
N = []
n = []
for c in range(C, -1, -1):
    complete = False
    v = '' 
    for r in range(0, R):
        #print(c,r, v, len(input[r]))
        if c < len(input[r]):
            if input[r][c] == '+' or input[r][c] == '*':
                n = [input[r][c]] + n          
                complete = True
            else:
                v += input[r][c].strip()
    if len(v) > 0:
        n.append(int(v))
    if complete:
        N.append(n)
        n = []
ans2 = 0
for ll in N:
    op = ll[0]
    v = 0 if op =='+' else 1
    for l in ll[1:]:
        if op == '+':
            v+=int(l)
        else:
            v *= int(l)
    ans2 += v

print('ans2', ans2)            
#print(N)
