#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,-1), (0, -1), (1, -1),(1, 0),(1, 1),(0, 1), (-1, 1),(-1,0)]

file1 = '4.in'
#file1 = '4.test'

input = [x.strip() for x in open(file1, 'r').readlines()]
G = []
for v in input:
   G.append(list(v))

def roles_to_remove(G):
    A = []
    R = len(G)
    C = len(G[0])
    for r in range(0, R):
        for c in range(0, C):
            if G[r][c] == '@':
                n = 0
                for rd, cd in D:
                    rr = r+rd
                    cc = c+cd
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == '@':
                        n += 1
                if n < 4:
                    A.append((r, c))
    return A

def remove_roles(G, A):
    R = len(G)
    C = len(G[0])
    for r in range(0, R):
        for c in range(0, C):
            if (r, c) in A:
                G[r][c] = '.'
    return G

print('ans1', len(roles_to_remove(G)))

A = roles_to_remove(G)
ans2 = len(A)
c = 0
while len(A) > 0:
    G = remove_roles(G, A)
    A = roles_to_remove(G)
    ans2 += len(A)
    print('iteration', c, len(A))
    c+=1 
print('ans2', ans2)
    

