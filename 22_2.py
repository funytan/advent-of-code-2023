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
sys.setrecursionlimit(10000)


with open('inputs/input_22.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    
    # parse inputs
    blocks_dic = {}
    blocks_base_dic = {}
    bases = []
    
    for idx, line in enumerate(lines, 1):
        s, e = line.split('~')
        s_x, s_y, s_z = s.split(',')
        s_x, s_y, s_z = int(s_x), int(s_y), int(s_z)
        e_x, e_y, e_z = e.split(',')
        e_x, e_y, e_z = int(e_x), int(e_y), int(e_z)
        
        blocks_dic[idx] = []
        blocks_base_dic[idx] = []
        
        # only 1 dimension changes
        if s_z != e_z:
            for z in range(s_z, e_z+1):
                blocks_dic[idx].append((s_x, s_y, z))
            blocks_base_dic[idx].append((s_x, s_y, min(s_z, e_z)))
            bases.append((min(s_z, e_z), idx))
        elif s_y != e_y:
            for y in range(s_y, e_y+1):
                blocks_dic[idx].append((s_x, y, s_z))
                blocks_base_dic[idx].append((s_x, y, s_z))
            bases.append((s_z, idx))
        elif s_x != e_x:
            for x in range(s_x, e_x+1):
                blocks_dic[idx].append((x, s_y, s_z))
                blocks_base_dic[idx].append((x, s_y, s_z))
            bases.append((s_z, idx))
        else:
            blocks_dic[idx].append((s_x, s_y, s_z))
            blocks_base_dic[idx].append((s_x, s_y, s_z))
            bases.append((s_z, idx))
            
        
    
    # iterate from the bottom
    bases = sorted(bases)
    floor_dic = defaultdict(int)
    floor_to_block_mapping = defaultdict(int)
    res = len(bases)
    unstable = set()
    supporting_dic = defaultdict(set)
    supported_dic = defaultdict(set)
    
    for _, idx in bases:
        block_bases = blocks_base_dic[idx]
        stable_height = 0
        stable_height_support = set()
        for block_base in block_bases:
            x, y, z = block_base
            indiv_stable_height = floor_dic[(x,y)] + 1
            if indiv_stable_height == stable_height:
                stable_height_support.add(floor_to_block_mapping[(x,y)])
            elif indiv_stable_height > stable_height:
                stable_height = indiv_stable_height
                stable_height_support = set([floor_to_block_mapping[(x,y)]])
        if 0 in stable_height_support:
            stable_height_support.remove(0)
        # find unstables ones
        stable_height_support = list(stable_height_support)
        if len(stable_height_support) == 1 :
            # print(stable_height_support[0])
            unstable.add(list(stable_height_support)[0])
        
        # update
        if len(block_bases) > 1: # flat block
            for block in blocks_dic[idx]:
                x, y, z = block
                assert stable_height > floor_dic[(x,y)]
                floor_dic[(x,y)] = stable_height
                floor_to_block_mapping[(x,y)] = idx
        else: # tall block
            assert len(block_bases) == 1
            x,y, _ = blocks_dic[idx][0]
            num_blocks = len(blocks_dic[idx])
            floor_to_block_mapping[(x,y)] = idx
            assert stable_height > floor_dic[(x,y)]
            floor_dic[(x,y)] = stable_height + num_blocks - 1
        
        for supporting_block in stable_height_support:
            supporting_dic[supporting_block].add(idx)
            supported_dic[idx].add(supporting_block)
    
    res = 0
    def find(node):
        temp = copy.deepcopy(supported_dic)
        deq = deque([node])
        ans = 0
        while deq:
            node = deq.popleft()
            for upper_node in supporting_dic[node]:
                temp[upper_node].remove(node)
                if len(temp[upper_node]) == 0:
                    ans += 1
                    deq.append(upper_node)
        return ans
            
    for node in unstable:
        res += find(node)
    
    print(res)
    print(len(bases) - len(unstable))
                
    
    # 104767 too high
            
            
            
        
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
                
   
        
        