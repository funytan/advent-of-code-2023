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
import numpy as np


with open('inputs/input_24.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    
    lines_processed = []
    
    for line in lines:
        points, vector = line.split('@')
        x, y, z = [int(point.strip()) for point in points.split(',')]
        d_x, d_y, d_z = [int(d.strip()) for d in vector.split(',')]
        
        lines_processed.append([x,y,z,d_x,d_y,d_z])
        
 
    
    def find_intersection_3d(point1, vector1, point2, vector2):
        # Convert input lists to NumPy arrays
        point1 = np.array(point1)
        vector1 = np.array(vector1)
        point2 = np.array(point2)
        vector2 = np.array(vector2)
    
        # Find the direction vectors of the lines
        direction1 = vector1 / np.linalg.norm(vector1)
        direction2 = vector2 / np.linalg.norm(vector2)
    
        # Check if the vectors are parallel
        if np.all(np.cross(direction1, direction2) == 0):
            return None
    
        # Find the parameter values for the intersection point
        t = np.dot(point2 - point1, np.cross(direction2, direction1)) / np.linalg.norm(np.cross(direction1, direction2))**2
    
        # Calculate the intersection point
        intersection_point = point1 + t * direction1
    
        return intersection_point

    def find_intersection_2d(x0a,y0a,dxa,dya,x0b,y0b,dxb,dyb):
        if dxa*dyb-dxb*dya == 0: 
            return (float('inf'), float('inf'))
        t = (dyb*(x0b-x0a)-dxb*(y0b-y0a))/(dxa*dyb-dxb*dya)
        u = (dya*(x0b-x0a)-dxa*(y0b-y0a))/(dxa*dyb-dxb*dya)
        if t >= 0 and u>=0: # ensure both are in present or future
            return (x0a+dxa*t,y0a+dya*t)
        else:
            return (float('inf'), float('inf'))
    
    x_min = 200000000000000
    x_max = 400000000000000
    y_min = 200000000000000
    y_max = 400000000000000
    
    res = 0
    
    for i in range(len(lines_processed)):
        x0a, y0a, z0a, dxa, dya, dza = lines_processed[i]
        for j in range(i+1, len(lines_processed)):
            x0b, y0b, z0b, dxb, dyb, dzb = lines_processed[j]
            i_x, i_y = find_intersection_2d(x0a,y0a,dxa,dya,x0b,y0b,dxb,dyb)
            if x_min<= i_x <= x_max and y_min<= i_y <= y_max:
                res += 1
        
    

    
    
    
    
    
    
    
    
    
            
                
   
        
        