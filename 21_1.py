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


with open('inputs/input_21.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    start = None
    direcs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for r in range(num_r):
        for c in range(num_c):
            if lines[r][c] == 'S':
                start = (r,c)
                break
        if start is not None:
            break
    
    stack = [start]
    steps = 64
    curr_step = 0 
    while curr_step<steps:
        new_stack = []
        for r,c in stack:
            for d in direcs:
                n_r, n_c = r+d[0], c+d[1]
                if 0<=n_r<num_r and 0<=n_c<num_c and (lines[n_r][n_c] == '.' or lines[n_r][n_c] == 'S'):
                    new_stack.append((n_r, n_c))
        new_stack = list(set(new_stack))
        stack = new_stack
        curr_step += 1
    
    print(len(stack))
    
    visited = set(stack)
    
    for r in range(num_r):
        row = []
        for c in range(num_c):
            row.append(lines[r][c])
            if (r,c) in visited:
                row[-1] = 'O'
        print(''.join(row))
                
        
        