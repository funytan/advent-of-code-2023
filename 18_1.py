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
from bisect import bisect_left, bisect_right
from functools import lru_cache

import sys
sys.setrecursionlimit(10000)


with open('inputs/input_18.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    direcs = {
        'U': (-1,0),
        'D': (1,0),
        'L': (0,-1),
        'R': (0,1),
    }
    
    curr = [0,0]
    dug = set([(0,0)])
    for line in lines:
        direc, length, color = line.split()
        length = int(length)
        d = direcs[direc]
        for i in range(length):
            curr[0], curr[1] = curr[0] + d[0], curr[1]+d[1]
            dug.add(tuple(curr))
    
    
    stack = [(1,-1)]
    while stack:
        r, c = stack.pop()
        for direc in direcs:
            d = direcs[direc]
            n_r, n_c = r + d[0], c+ d[1]
            if (n_r, n_c) not in dug:
                dug.add((n_r, n_c))
                stack.append((n_r, n_c))
    print(len(dug))
    # print(res)
    # 127 93 161 93
    #10 3 17 3