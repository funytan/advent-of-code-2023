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



with open('inputs/input_16.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])   
    stack = [('E', 0, -1)]
    visited = set()
    visited_with_direc = set()
    
    while stack:
        direc, r, c = stack.pop()
        visited.add((r,c))
        if (direc, r,c) not in visited_with_direc:
            visited_with_direc.add((direc,r,c))
        else:
            continue
        if direc == 'E':
            n_r, n_c = r, c+1
            if 0<=n_r<num_r and 0<=n_c < num_c:
                ch = lines[n_r][n_c]
                if ch == '|':
                    stack.append(('N', n_r, n_c))
                    stack.append(('S', n_r, n_c))
                elif ch == "\\":
                    stack.append(('S', n_r, n_c))
                elif ch == '/':
                    stack.append(('N', n_r, n_c))
                else:
                    stack.append(('E', n_r, n_c))
        if direc == 'S':
            n_r, n_c = r+1, c
            if 0<=n_r<num_r and 0<=n_c< num_c:
                ch = lines[n_r][n_c]
                if ch == '-':
                    stack.append(('E', n_r, n_c))
                    stack.append(('W', n_r, n_c))
                elif ch == '\\':
                    stack.append(('E', n_r, n_c))
                elif ch == '/':
                    stack.append(('W', n_r, n_c))
                else:
                    stack.append(('S', n_r, n_c))
        if direc == 'W':
            n_r, n_c = r, c-1
            if 0<=n_r<num_r and 0<=n_c< num_c:
                ch = lines[n_r][n_c]
                if ch == '|':
                    stack.append(('N', n_r, n_c))
                    stack.append(('S', n_r, n_c))
                elif ch == '\\':
                    stack.append(('N', n_r, n_c))
                elif ch == '/':
                    stack.append(('S', n_r, n_c))
                else:
                    stack.append(('W', n_r, n_c))
        if direc == 'N':
            n_r, n_c = r-1, c
            if 0<=n_r<num_r and 0<=n_c< num_c:
                ch = lines[n_r][n_c]
                if ch == '-':
                    stack.append(('E', n_r, n_c))
                    stack.append(('W', n_r, n_c))
                elif ch == '\\':
                    stack.append(('W', n_r, n_c))
                elif ch == '/':
                    stack.append(('E', n_r, n_c))
                else:
                    stack.append(('N', n_r, n_c))
    # for i in range(num_r):
    #     row = ''
    #     for j in range(num_c):
    #         if (i,j) not in visited:
    #             row += '.'
    #         else:
    #             row += '#'
    #     print(row)
    # print()
                
    print(len(visited)-1)
    # 127 93 161 93
    #10 3 17 3