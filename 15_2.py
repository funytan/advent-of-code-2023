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
    boxes = defaultdict(dict)
    boxes_order = defaultdict(int)
    
    
    for s in string_ls:
        curr = 0
        add = False
        if s[-1] == '-':
            lens = s[:-1]
        else:
            lens = s[:-2]
            add = True
            focal_length = int(s[-1])
        for ch in lens:
            curr += ord(ch)
            curr *= 17
            curr %= 256
        if add:
            if lens in boxes[curr]:
                boxes[curr][lens][0] = focal_length
            else:
                boxes[curr][lens] = [focal_length, boxes_order[curr]]
                boxes_order[curr] += 1                
        else:
            if lens in boxes[curr]:
                del boxes[curr][lens]
    
    for box in boxes:
        ls = [boxes[box][lens] for lens in boxes[box]]
        ls = sorted(ls, key=lambda x: x[1])
        for slot, item in enumerate(ls,1):
            res += (1+box) * slot * item[0]
        
    
    
    print(res)
    # 127 93 161 93
    #10 3 17 3