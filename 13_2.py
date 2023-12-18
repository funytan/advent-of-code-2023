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



with open('inputs/input_13.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    idx = 0
    
    def check_str(a, b):
        errors = 0
        for ch_a, ch_b in zip(a,b):
            if ch_a != ch_b:
                errors += 1
        return errors
    
    def find(mat):
        num_r = len(mat)
        num_c = len(mat[0])
        for i in range(num_r-1):
            up = i
            down = i+1
            errors = 0
            while errors<=1 and up>=0 and down<num_r:
                errors += check_str(mat[up], mat[down])
                up -= 1
                down += 1
            if errors==1:
                return (i+1)*100
            
        for j in range(num_c-1):
            left = j
            right = j+1
            errors = 0
            while errors<=1 and left>=0 and right<num_c:
                left_str = ''.join([mat[r][left] for r in range(num_r)])
                right_str = ''.join([mat[r][right] for r in range(num_r)])
                errors += check_str(left_str, right_str)
                left -= 1
                right += 1
            if errors==1:
                return (j+1)
            # if j==6:
                # print(errors)
            
        assert 1==2
    
    while idx < len(lines):
        curr = []
        while idx < len(lines) and lines[idx] != '':
            curr.append(lines[idx])
            idx += 1
        res += find(curr)
        idx += 1
        
        
    print(res)