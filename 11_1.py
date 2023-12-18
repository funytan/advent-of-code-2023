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

with open('inputs/input_11.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    mat = []
    empty_row = []
    empty_col = []
    galaxies = []
    
    for line in lines:
        mat.append(line)

    num_r = len(mat)
    num_c = len(mat[0])
        
    for i in range(num_r):
        galaxy_found = False
        for j in range(num_c):
            ch = mat[i][j]
            if ch == '#':
                galaxy_found = True
                galaxies.append((i, j))
        if not galaxy_found:
            empty_row.append(i)

    for j in range(num_c):
        galaxy_found = False
        for i in range(num_r):
            ch = mat[i][j]
            if ch == '#':
                galaxy_found = True
        if not galaxy_found:
            empty_col.append(j)
            
    res = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            r1, c1 = galaxies[i]
            r2, c2 = galaxies[j]
            res += abs(r1-r2)
            res += abs(c1-c2)
            idx1 = bisect_left(empty_row, r1)
            idx2 = bisect_left(empty_row, r2)
            res += abs(idx1-idx2)
            idx1 = bisect_left(empty_col, c1)
            idx2 = bisect_left(empty_col, c2)
            res += abs(idx1-idx2)
    print(res)