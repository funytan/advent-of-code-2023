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
import math

import sys
import numpy as np
from sympy.ntheory.modular import solve_congruence

# chinese remainder theorem

with open('inputs/input_24.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    
    lines_processed = []
    
    for line in lines:
        points, vector = line.split('@')
        x, y, z = [int(point.strip()) for point in points.split(',')]
        d_x, d_y, d_z = [int(d.strip()) for d in vector.split(',')]
        
        lines_processed.append([x,y,z,d_x,d_y,d_z])
    
    
    x_lines = sorted([(item[0], item[3], idx) for idx, item in enumerate(lines_processed)])
    y_lines = sorted([(item[1], item[4], idx) for idx, item in enumerate(lines_processed)])
    z_lines = sorted([(item[2], item[5], idx) for idx, item in enumerate(lines_processed)])
        
    
    result_x_ls = []
    
    for v in range(-500, 501):
        congruences = [(item[0] %(v - item[1]), v - item[1]) for item in x_lines if v - item[1] != 0]
        result = solve_congruence(*congruences)
        if result is not None:
            result_x_ls.append((result[0], result[1], v))
    
    
    x_start = 369109345096355
    x_vel = -153
    
    result_y_ls = []
    
    for v in range(-700, 701):
        congruences = [(item[0] %(v - item[1]), v - item[1]) for item in y_lines if v - item[1] != 0]
        result = solve_congruence(*congruences)
        if result is not None:
            result_y_ls.append((result[0], result[1], v))
    
    y_start = 377478862726817
    y_vel = -150
    

    result_z_ls = []
    
    for v in range(-700, 701):
        congruences = [(item[0] %(v - item[1]), v - item[1]) for item in z_lines if v - item[1] != 0]
        result = solve_congruence(*congruences)
        if result is not None:
            result_z_ls.append((result[0], result[1], v))
    
    z_start = 138505253617233
    z_vel = 296
    
    time_taken_x = []
    for item in x_lines:
        if (x_vel-item[1]):
            t = (item[0]-x_start)/(x_vel-item[1]) 
        else:
            t = 0
        time_taken_x.append((t, item[2]))
    
    time_taken_x = sorted(time_taken_x)

    time_taken_y = []
    for item in y_lines:
        if (y_vel-item[1]):
            t = (item[0]-y_start)/(y_vel-item[1]) 
        else:
            t = 0
        time_taken_y.append((t, item[2]))
    
    time_taken_y = sorted(time_taken_y)
    
    time_taken_z = []
    for item in z_lines:
        if (z_vel-item[1]):
            t = (item[0]-z_start)/(z_vel-item[1]) 
        else:
            t = 0
        time_taken_z.append((t, item[2]))
    
    time_taken_z = sorted(time_taken_z)