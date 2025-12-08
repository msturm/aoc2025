#!/usr/bin/env python3
import re
from collections import defaultdict
from collections import deque

def nums(v):
	return [int(x) for x in re.findall(r"\d+",v)]

D = [(-1,0), (0, 1), (1, 0), (0,-1)]

file1 = '3.in'

input = [x.strip() for x in open(file1, 'r').readlines()]
for v in input:
