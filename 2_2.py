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

            
with open('inputs/input_2.txt', 'r') as f:
    lines = f.readlines()
    res = 0
    for idx, line in enumerate(lines, 1):
        picks = line.split(':')[1].strip()
        curr = defaultdict(int)
        for pick in picks.split(';'):
            for pick_color in pick.split(','):
                pick_color = pick_color.strip()
                num, color = pick_color.split()
                num = int(num)
                curr[color] = max(curr[color], num)
        power = curr['red'] * curr['green'] * curr['blue']
        res += power
        print(res)