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

pipes = {
    '|' : {(1,0): (1,0), (-1,0): (-1,0)},
   '-' : {(0,1): (0,1), (0,-1): (0,-1)},
    'L' : {(1,0): (0,1), (0,-1): (-1,0)},
    'J' : {(1,0): (0,-1), (0,1): (-1,0)},
    '7' : {(-1,0): (0,-1), (0,1): (1,0)},
    'F' : {(-1,0): (0,1), (0,-1): (1,0)},
    '.' : None    
}
            
with open('inputs/input_10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    mat = []
    for line in lines:
        mat.append(line)
        num_r = len(mat)
        num_c = len(mat[0])
    
    res = 0
    for r in range(num_r):
        for c in range(num_c):
            # print(r, c)
            if mat[r][c] == 'S' or mat[r][c] == '.':
                continue
            curr_r = r
            curr_c = c
            stack = []
            steps = 0
            visited = set()
            for direc in pipes[mat[curr_r][curr_c]]:
                direc = pipes[mat[curr_r][curr_c]][direc]
                n_r , n_c = curr_r + direc[0], curr_c + direc[1]
                if 0<=n_r<num_r and 0<=n_c<num_c and mat[n_r][n_c] != '.':
                    stack.append((n_r, n_c, direc)) # location, prev_direc
                    visited.add((n_r, n_c))
            if stack:
                steps += 1
            check = True
            visited = set()
            
            while stack and check:
                # print(stack, steps)
                new_stack = []
                for curr_r, curr_c, prev_direc in stack:
                    # print(mat[curr_r][curr_c])
                    if mat[curr_r][curr_c] == 'S':
                        check = False
                        break
                    if prev_direc in pipes[mat[curr_r][curr_c]]:
                        direc = pipes[mat[curr_r][curr_c]][prev_direc]
                        n_r , n_c = curr_r + direc[0], curr_c + direc[1]
                        if 0<=n_r<num_r and 0<=n_c<num_c and mat[n_r][n_c] != '.' and (n_r, n_c) not in visited:
                            new_stack.append((n_r, n_c, direc))
                            visited.add((n_r, n_c))
                stack = new_stack
                if check:
                    steps += 1
            if not check:
                res = max(res, steps)
    print(res)