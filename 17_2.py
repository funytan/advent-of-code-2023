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


with open('inputs/input_17.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = float('inf')
    num_r = len(lines)
    num_c = len(lines[0]) 
    direcs = {
        'N': (-1,0),
        'S': (1,0),
        'E': (0,1),
        'W': (0,-1),
        
    }
    
    lines = [[int(ch) for ch in line]for line in lines]
    
    heap = [(lines[0][1],0,1,'E',9), (lines[1][0],1,0,'S',9)]
    visited = set(
        [(0,1,'E',9), 
         (1,0,'S',9)]
    )
    check = True
    while len(heap) and check:
        cost, r,c, direc, left = heappop(heap)
        # print(cost, r, c, direc, left)
        if r == (num_r-1) and c ==(num_c-1) and left<=6:
            res = cost
            break
        else:
            if left > 6:
                n_r, n_c = r+direcs[direc][0], c+direcs[direc][1]
                if 0<=n_r<num_r and 0<=n_c<num_c:
                    n_cost = cost + lines[n_r][n_c]
                    if (n_r, n_c, direc, left-1) not in visited:
                        visited.add((n_r, n_c, direc, left-1))
                        heappush(heap, (n_cost, n_r, n_c, direc, left-1))
            else:
                for n_direc in direcs:
                    if left == 0 and n_direc == direc:
                        continue
                    if n_direc == 'N' and direc == 'S':
                        continue
                    if n_direc == 'S' and direc == 'N':
                        continue
                    if n_direc == 'E' and direc == 'W':
                        continue
                    if n_direc == 'W' and direc == 'E':
                        continue
                    d = direcs[n_direc]
                    n_r, n_c = r + d[0], c+ d[1]
                    if 0<=n_r<num_r and 0<=n_c<num_c:
                        n_cost = cost + lines[n_r][n_c]
                        if direc == n_direc:
                            if (n_r, n_c, n_direc, left-1) not in visited:
                                visited.add((n_r, n_c, n_direc, left-1))
                                heappush(heap, (n_cost, n_r, n_c, n_direc, left-1))
                        else:
                            if (n_r, n_c, n_direc, 9) not in visited:
                                visited.add((n_r, n_c, n_direc, 9))
                                heappush(heap, (n_cost, n_r, n_c, n_direc, 9))
        
        # if cost > 20:
        #     break
    print(res)
    # 127 93 161 93
    #10 3 17 3