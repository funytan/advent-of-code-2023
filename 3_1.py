import io, os, sys
from sys import stdin, stdout
 
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
# def read_int_list(): return list(map(int, input().split()))
# def read_int_tuple(): return tuple(map(int, input().split()))
# def read_int(): return int(input())
 
from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache

            
with open('inputs/input_3.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    hits = set()
    direcs = [
        (0,1),
        (1,1),
        (1,0),
        (-1,0),
        (0,-1),
        (-1,-1),
        (1,-1),
        (-1,1),
    ]
    num_r = len(lines)
    num_c = len(lines[0])
    
    for i, line in enumerate(lines, 1):
        for j, ch in enumerate(line):
            if (not '0'<=ch<='9') and (ch!='.'):
                for direc in direcs:
                    n_i, n_j = i + direc[0], j+direc[1]
                    hits.add((n_i, n_j))
    
    curr = 0
    found = False
    for i, line in enumerate(lines, 1):
        for j, ch in enumerate(line):
            if '0'<=ch<='9':
                curr *= 10
                curr += int(ch)
                if (i,j) in hits:
                    found = True
            else:
                if found:
                    res += curr
                    found = False
                curr = 0
    if found:
        res += curr
    
    print(res)