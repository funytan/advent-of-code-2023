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
import copy

import sys
sys.setrecursionlimit(10000)


with open('inputs/input_23.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    start = (0,1)
    end = (num_r-1, num_c-2)
    direcs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    stack = [(start, set([start]))]
    
    def dfs(node, visited):
        # print(node)
        r, c = node
        if (r, c) == end:
            return 0
        ans = float('-inf')
        ch = lines[r][c]
        if ch == '.':
            # print('here')
            for d in direcs:
                n_r, n_c = r + d[0], c+ d[1]
                if 0<=n_r<num_r and 0<=n_c<num_c and lines[n_r][n_c] != '#' and (n_r, n_c) not in visited:
                    visited.add((n_r, n_c))
                    ans = max(ans, dfs((n_r, n_c), visited))
                    visited.remove((n_r, n_c))
        else:
            if ch == '^':
                d = (-1,0)
            elif ch == '<':
                d = (0,-1)
            elif ch == '>':
                d = (0,1)
            elif ch == 'v':
                d = (1,0)
            n_r, n_c = r + d[0], c+ d[1]
            if 0<=n_r<num_r and 0<=n_c<num_c and lines[n_r][n_c] != '#' and (n_r, n_c) not in visited:
                visited.add((n_r, n_c))
                ans = max(ans, dfs((n_r, n_c), visited))
                visited.remove((n_r, n_c))
        return 1+ans
    
    res = dfs(start, set([start]))
                
            
            
        
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
                
   
        
        