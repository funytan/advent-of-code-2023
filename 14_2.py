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



with open('inputs/input_14.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    mat = []
    fixed_row =defaultdict(list)
    fixed_col = defaultdict(list)
    rocks_row = defaultdict(list)
    rocks_col = defaultdict(list)
    
    for line in lines:
        mat.append(line)
        
        
    for i in range(num_r):
        for j in range(num_c):
            if mat[i][j] == '#':
                fixed_row[i].append(j)
                fixed_col[j].append(i)
            elif mat[i][j] == 'O':
                rocks_row[i].append(j)
                rocks_col[j].append(i)
    
    check = True
    mem = {}
    cnt = 0
    while check and cnt < 13:
        # roll north
        prev = 0
        new_rocks_row = defaultdict(list)
        new_rocks_col = defaultdict(list)
        for j in range(num_c):
            rock_idx = 0
            fixed_idx = 0
            prev = 0
            while rock_idx < len(rocks_col[j]):
                rock = rocks_col[j][rock_idx]
                if fixed_idx<len(fixed_col[j]):
                    fixed = fixed_col[j][fixed_idx]
                else:
                    fixed = float('inf')
                if rock < fixed:
                    new_rocks_row[prev].append(j)
                    new_rocks_col[j].append(prev)
                    rock_idx += 1
                    prev += 1
                else:
                    prev = fixed + 1
                    fixed_idx += 1
        
        for i in range(num_r):
            if i in new_rocks_row:
                rocks_row[i] = sorted(new_rocks_row[i])
            else:
                rocks_row[i] = []
        for j in range(num_c):
            if j in new_rocks_col:
                rocks_col[j] = sorted(new_rocks_col[j])
            else:
                rocks_col[j] = []
        # roll west
        prev = 0
        new_rocks_row = defaultdict(list)
        new_rocks_col = defaultdict(list)
        for i in range(num_r):
            rock_idx = 0
            fixed_idx = 0
            prev = 0
            while rock_idx < len(rocks_row[i]):
                rock = rocks_row[i][rock_idx]
                if fixed_idx<len(fixed_row[i]):
                    fixed = fixed_row[i][fixed_idx]
                else:
                    fixed = float('inf')
                if rock < fixed:
                    new_rocks_row[i].append(prev)
                    new_rocks_col[prev].append(i)
                    rock_idx += 1
                    prev += 1
                else:
                    prev = fixed + 1
                    fixed_idx += 1
        for i in range(num_r):
            if i in new_rocks_row:
                rocks_row[i] = sorted(new_rocks_row[i])
            else:
                rocks_row[i] = []
        for j in range(num_c):
            if j in new_rocks_col:
                rocks_col[j] = sorted(new_rocks_col[j])
            else:
                rocks_col[j] = []
        # roll south
        new_rocks_row = defaultdict(list)
        new_rocks_col = defaultdict(list)
        for j in range(num_c -1,-1,-1):
            rock_idx = len(rocks_col[j]) - 1
            fixed_idx = len(fixed_col[j]) - 1
            prev = num_r-1
            while rock_idx >= 0:
                rock = rocks_col[j][rock_idx]
                if fixed_idx>=0:
                    fixed = fixed_col[j][fixed_idx]
                else:
                    fixed = -1
                if rock > fixed:
                    new_rocks_row[prev].append(j)
                    new_rocks_col[j].append(prev)
                    rock_idx -=1
                    prev -= 1
                else:
                    prev = fixed-1
                    fixed_idx -= 1
        for i in range(num_r):
            if i in new_rocks_row:
                rocks_row[i] = sorted(new_rocks_row[i])
            else:
                rocks_row[i] = []
        for j in range(num_c):
            if j in new_rocks_col:
                rocks_col[j] = sorted(new_rocks_col[j])
            else:
                rocks_col[j] = []
        # roll east
        new_rocks_row = defaultdict(list)
        new_rocks_col = defaultdict(list)
        for i in range(num_r-1,-1,-1):
            rock_idx = len(rocks_row[i])-1
            fixed_idx = len(fixed_row[i])-1
            prev = num_c-1
            while rock_idx >= 0:
                rock = rocks_row[i][rock_idx]
                if fixed_idx>=0:
                    fixed = fixed_row[i][fixed_idx]
                else:
                    fixed = -1
                if rock > fixed:
                    new_rocks_row[i].append(prev)
                    new_rocks_col[prev].append(i)
                    rock_idx -=1
                    prev -= 1
                else:
                    prev = fixed - 1
                    fixed_idx -= 1
        for i in range(num_r):
            if i in new_rocks_row:
                rocks_row[i] = sorted(new_rocks_row[i])
            else:
                rocks_row[i] = []
        for j in range(num_c):
            if j in new_rocks_col:
                rocks_col[j] = sorted(new_rocks_col[j])
            else:
                rocks_col[j] = []
        
        
        cnt += 1
        rocks = []
        for i in range(num_r):
            for j in rocks_row[i]:
                rocks.append((i,j))
        rocks = tuple(sorted(rocks))
        if rocks not in mem:
            mem[rocks] = cnt
        else:
            print(cnt, 'here', mem[rocks])
            
            
    
    for i in range(num_r):
        res +=(num_r - i) * len(new_rocks_row[i])
        
    print(res)
    # 127 93 161 93
    #10 3 17 3