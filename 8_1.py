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
            
            
with open('inputs/input_8.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    directions = lines[0]
    adj  = {}
    for line in lines[2:]:
        origin, dest = line.split(' = ')
        left = dest[1:4]
        right = dest[6:9]
        adj[origin] = (left, right)
    
    steps_to_zzz = {}
    one_run_dict = {}
    for origin in adj.keys():
        curr = origin
        for steps, d in enumerate(directions,1):
            if d == 'L':
                curr = adj[curr][0]
            else:
                curr = adj[curr][1]
            if curr == 'ZZZ':
                steps_to_zzz[origin] = steps

        one_run_dict[origin] = curr
    
    curr = 'AAA'
    ans = 0
    while curr not in steps_to_zzz:
        curr = one_run_dict[curr]
        ans += len(directions)
    
    ans += steps_to_zzz[curr]
    print(ans)