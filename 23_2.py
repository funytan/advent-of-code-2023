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

# path shortening

with open('inputs/input_23.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    start = (0,1)
    end = (num_r-1, num_c-2)
    direcs = [(0,1), (0,-1), (1,0), (-1,0)]
    
    entrypoints = set()
    entrypoints.add(start)
    entrypoints.add(end)
    
    for r in range(num_r):
        for c in range(num_c):
            if lines[r][c] == '#':
                continue
            count = 0
            for d in direcs:
                n_r, n_c = r + d[0], c+ d[1]
                if 0<=n_r<num_r and 0<=n_c<num_c and lines[n_r][n_c] != '#':
                    count += 1
            if count>2:
                entrypoints.add((r,c))
    
    adj_dic = defaultdict(list)
    
    def bfs(node):
        stack = [node]
        steps = 0
        visited = set([node])
        while stack:
            # print(stack)
            steps += 1
            new_stack = []
            for r,c in stack:
                for d in direcs:
                    n_r, n_c = r + d[0], c+ d[1]
                    n_node = (n_r, n_c)
                    if 0<=n_r<num_r and 0<=n_c<num_c and lines[n_r][n_c] != '#' and n_node not in visited:
                        if n_node in entrypoints:
                            adj_dic[node].append((n_r, n_c, steps))
                        else:
                            new_stack.append(n_node)
                            visited.add(n_node)
            stack = new_stack

                    
    for r, c in entrypoints:
        bfs((r,c))
    
    
    def dfs(node, visited):
        r, c = node
        if (r, c) == end:
            return 0
        ans = float('-inf')
        for item in adj_dic[node]:
            n_r, n_c, steps = item
            n_node = (n_r, n_c)
            if 0<=n_r<num_r and 0<=n_c<num_c and n_node not in visited:
                visited.add(n_node)
                ans = max(ans, dfs(n_node, visited)+steps)
                visited.remove(n_node)
        return ans
    
    res = dfs(start, set([start]))
 
    
    
    
    
    
    
    
    
    
    
            
                
   
        
        