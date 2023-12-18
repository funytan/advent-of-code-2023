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
    
    direc_map = ['R', 'D', 'L', 'U']
    
    
    vertical_ranges = [] # ordered by row number
    horizontal_changes = []
    curr = [0,0]
    for line in lines:
        _,_, code = line.split()
        r, c = curr
        code = code[1:-1]
        direc = direc_map[int(code[-1])]
        dist = int(code[1:-1], 16)
        d = direcs[direc]
        n_r, n_c = d[0]* dist + r, d[1]* dist+c
        if direc == 'U' or direc=='D':
            if direc == 'U':
                vertical_ranges.append((n_r, r, c))
            if direc == 'D':
                # print('here', r, c)
                vertical_ranges.append((r, n_r, c))
        else:
            horizontal_changes.append(r)
        curr[0], curr[1] = n_r, n_c
    
    def find_verts(r):
        ls = []
        for v_range in vertical_ranges:
            s, e, c = v_range
            if s<=r<=e:
                ls.append((c))
        ls = sorted(ls)
        # print(len(ls), ls, r)
        assert len(ls)%2 == 0
        ans = 0
        ranges = []
        for i in range(0, len(ls), 2):
            ans += ls[i+1] - ls[i] + 1
            ranges.append((ls[i], ls[i+1]))
        return ans, ranges
    
    def merge_ranges(l_ls, r_ls):
        merged_list = l_ls + r_ls
    
        merged_list.sort(key=lambda x: x[0])
    
        result = []
    
        for range_ in merged_list:
            if not result or result[-1][1] < range_[0]:
                result.append(range_)
            else:
                result[-1] = (result[-1][0], max(result[-1][1], range_[1]))
        
        ans = 0
        for r in result:
            ans += r[1] - r[0] + 1
        return ans
        
        
    
    horizontal_changes = sorted(list(set(horizontal_changes)))
    curr_r = horizontal_changes[0]
    prev_width, prev_ls = find_verts(curr_r)
    res = 0
    for r in horizontal_changes[1:-1]:
        print(r)
        if curr_r == horizontal_changes[0]:
            vert_dist = r - curr_r
        else:
            vert_dist = r - curr_r - 1 # not include transition point
        
        res += prev_width*vert_dist
        new_width, new_ls = find_verts(r+1)
        res += merge_ranges(prev_ls, new_ls) # for one row
        
        prev_width = new_width
        curr_r = r
        prev_ls = new_ls
        
    # do for last row
    r = horizontal_changes[-1]
    vert_dist = r - curr_r
    res += prev_width*vert_dist
    
    print(res)
        
    
    # print(len(dug))
    # print(res)
    # 127 93 161 93
    #10 3 17 3