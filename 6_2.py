import io, os, sys
from sys import stdin, stdout
 
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
# def read_int_list(): return list(map(int, input().split()))
# def read_int_tuple(): return tuple(map(int, input().split()))
# def read_int(): return int(input())
 
from itertools import permutations, chain, combinations, product
from math import factorial, gcd, ceil
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache


perturb = 0.01 # add to distance to avoid checking case where distance travelled is equal. Since time is always a whole number, it is guaranteed that the perturbation will not change the results when rounding.
with open('inputs/input_6.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    time = int(''.join(lines[0].split(':')[1].strip().split()))
    dist = int(''.join(lines[1].split(':')[1].strip().split()))
    dist +=  perturb
    slack = (time/2)**2 - dist
    slack_sqrt = slack**(0.5)
    r = [ceil(time/2-slack_sqrt), int(time/2 + slack_sqrt)]
    ans = (r[1] - r[0] + 1)
    print(ans)