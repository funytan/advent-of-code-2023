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


with open('inputs/input_12.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    
    @lru_cache
    def find(r1, r2, idx_1, idx_2):
        # print(r1, r2, r1[idx_1:], r2[idx_2:])
        if idx_1 >= len(r1):
            if idx_2 < len(r2):
                return 0
            else:
                return 1
        if idx_2 == len(r2):
            if '#' in r1[idx_1:]:
                return 0
            else:
                return 1
        ans = 0
        if r1[idx_1] != '.':
            group_len = r2[idx_2]
            if (
                    (group_len + idx_1) <= len(r1) and 
                    all([(ch=='?') or (ch=='#') for ch in r1[idx_1:idx_1+group_len]]) and
                    (idx_1+group_len == len(r1) or r1[idx_1+group_len] != '#')
                ):
                        ans += find(r1, r2, idx_1+group_len+1, idx_2+1)
        if r1[idx_1] != '#':
            ans += find(r1, r2, idx_1+1, idx_2)
        return ans
    
    for line in lines:
        r1, r2 = line.split()
        r2 = tuple(map(int, r2.split(',')))
        r1 = ((r1 + '?')*5)[:-1]
        r2 = r2 * 5
        res += find(r1, r2, 0, 0)

    print(res)