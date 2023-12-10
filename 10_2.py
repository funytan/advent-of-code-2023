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

l_hand = {
    '|' : {(1,0): [(0,1)], (-1,0): [(0,-1)]},
    '-' : {(0,1): [(-1,0)], (0,-1): [(1,0)]},
    'L' : {(1,0): [], (0,-1): [(1,0),(1,-1),(0,-1)]},
    'J' : {(1,0): [(0,1), (1,0), (1,1)], (0,1): []},
    '7' : {(-1,0): [], (0,1): [(-1,0), (-1,1), (0,1)]},
    'F' : {(-1,0): [(0,-1), (-1,-1), (-1,0)], (0,-1): []},
}

r_hand = {
    '|' : {(1,0): [(0,-1)], (-1,0): [(0,1)]},
    '-' : {(0,1): [(1,0)], (0,-1): [(-1,0)]},
    'L' : {(1,0): [(1,0),(1,-1),(0,-1)], (0,-1): []},
    'J' : {(1,0): [], (0,1): [(0,1), (1,0), (1,1)]},
    '7' : {(-1,0): [(-1,0), (-1,1), (0,1)], (0,1): []},
    'F' : {(-1,0): [], (0,-1): [(0,-1), (-1,-1), (-1,0)]},
}
            
with open('inputs/input_10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    mat = []
    for line in lines:
        mat.append(line)
        num_r = len(mat)
        num_c = len(mat[0])
    
    in_loop = set()
    not_in_loop = set()
    right_b =set()
    left_b = set()
    for r in range(num_r):
        for c in range(num_c):
            # print(r, c)
            if (r,c) in  not_in_loop or (r,c) in  not_in_loop:
                continue
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
            
            while stack:
                new_stack = []
                for curr_r, curr_c, prev_direc in stack:
                    if mat[curr_r][curr_c] == 'S':
                        check = False
                        last_seen = (
                            curr_r - prev_direc[0], 
                            curr_c - prev_direc[1], 
                            (- prev_direc[0], - prev_direc[1])
                        )
                        continue
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
                in_loop = in_loop.union(visited)
                break
            else:
                not_in_loop = not_in_loop.union(visited)
    
    stack = [last_seen]
    while stack:
        new_stack = []
        for curr_r, curr_c, prev_direc in stack:
            if mat[curr_r][curr_c] == 'S':
                check = False
                continue
            if prev_direc in pipes[mat[curr_r][curr_c]]:
                r_d = r_hand[mat[curr_r][curr_c]][prev_direc]
                for d in r_d:
                    right_b.add((curr_r +d[0], curr_c + d[1]))
                l_d = l_hand[mat[curr_r][curr_c]][prev_direc]
                for d in l_d:
                    left_b.add((curr_r +d[0], curr_c + d[1]))
                
                direc = pipes[mat[curr_r][curr_c]][prev_direc]
                n_r , n_c = curr_r + direc[0], curr_c + direc[1]
                new_stack.append((n_r, n_c, direc))
        stack = new_stack

    direcs = [(0,1), (1,0), (0,-1), (-1,0)]
    l_res = 0
    visited = set().union(in_loop)
    for r, c in left_b:
        if (r,c) in visited:
            continue
        stack = [(r,c)]
        visited.add((r,c))
        while stack:
            new_stack = []
            for curr_r, curr_c in stack:
                l_res += 1
                for d in direcs:
                    n_r, n_c = curr_r + d[0], curr_c + d[1]
                    if 0<=n_r<num_r and 0<=n_c<num_c and (n_r, n_c) not in visited:
                        new_stack.append((n_r, n_c))
                        visited.add((n_r,n_c))
            stack = new_stack
    # print(len(visited))
    r_res = 0
    visited = set().union(in_loop)
    for r, c in right_b:
        if (r,c) in visited:
            continue
        stack = [(r,c)]
        visited.add((r,c))
        while stack:
            new_stack = []
            for curr_r, curr_c in stack:
                r_res += 1
                for d in direcs:
                    n_r, n_c = curr_r + d[0], curr_c + d[1]
                    if 0<=n_r<num_r and 0<=n_c<num_c and (n_r, n_c) not in visited:
                        new_stack.append((n_r, n_c))
                        visited.add((n_r,n_c))
            stack = new_stack
    
            
    print(l_res, r_res) # the answer is one of them
    
    # for r in range(num_r):
    #     row = ''
    #     for c in range(num_c):
    #         if (r,c) in left_b:
    #             row += '*'
    #         else:
    #             row += '.'
    #     print(row)