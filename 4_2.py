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

            
with open('inputs/input_4.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    copies = {i: 1 for i in range(len(lines))}
    
    for i, line in enumerate(lines):
        _, numbers = line.split(': ')
        winning, curr = numbers.split(' | ')
        win_num_set = set()
        hit = 0
        for num in winning.split():
            num = int(num)
            win_num_set.add(num)
        for num in curr.split():
            num = int(num)
            if num in win_num_set:
                hit += 1
        
        for j in range(hit):
            copies[i+j+1] += copies[i]
            

    print(sum([copies[key] for key in copies]))