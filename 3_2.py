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
    part_num_dic = {}
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
    
    curr = 0
    stack = []
    
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if '0'<=ch<='9':
                curr *= 10
                curr += int(ch)
                stack.append((i,j))
            else:
                if stack:
                    root_x, root_y = stack[0][0], stack[0][1] # unique identifier
                while stack:
                    loc = stack.pop()
                    part_num_dic[loc] = (curr, root_x, root_y) 
                curr = 0
                stack = []
    if stack:
        root_x, root_y = stack[0][0], stack[0][1] # unique identifier
    while stack:
        loc = stack.pop()
        part_num_dic[loc] = (curr, root_x, root_y) 
    
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if (not '0'<=ch<='9') and (ch!='.'):
                adj_ls = set()
                for direc in direcs:
                    n_i, n_j = i + direc[0], j+direc[1]
                    if (n_i, n_j) in part_num_dic:
                        adj_ls.add(part_num_dic[(n_i, n_j)])
                if len(adj_ls) == 2:
                    # print(i,j, adj_ls)
                    adj_ls = list(adj_ls)
                    res += adj_ls[0][0] * adj_ls[1][0]



    print(res)