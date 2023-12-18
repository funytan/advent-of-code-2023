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



with open('inputs/input_15.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    string_ls = lines[0].split(',')
    
    
    for s in string_ls:
        curr = 0
        for ch in s:
            curr += ord(ch)
            curr *= 17
            curr %= 256
        res += curr
    
    
    print(res)
    # 127 93 161 93
    #10 3 17 3