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
from itertools import combinations
import tqdm

with open('inputs/input_25.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    adj_dict = defaultdict(set)
    ls = []
    
    for line in lines:
        u, vs = line.split(': ')
        vs = vs.split()
        for v in vs:
            adj_dict[u].add(v)
            adj_dict[v].add(u)
    
    assert min([len(adj_dict[k]) for k in adj_dict]) > 3
    
    def path_len(nodes, par_node):
        # print(nodes, par_node)
        res = {}
        for i, u in enumerate(nodes):
            sum_len = 0
            for j, v in enumerate(nodes):
                visited = set([u, par_node])
                if u == v:
                    continue
                stack = [u]
                length = 0
                while stack: 
                    new_stack = []
                    for node in stack:
                        if node == v:
                            sum_len += length
                            break
                        for n_node in adj_dict[node]:
                            if n_node not in visited:
                                visited.add(n_node)
                                new_stack.append(n_node)
                    stack = new_stack
                    length+=1
            # print(sum_len, u, par_node)
            res[u] = sum_len
        return res

    child_path_lens = []
    nodes = list(adj_dict.keys())
    
    candidates = []
    for node in nodes:
        dic =path_len(adj_dict[node], node)
        max_key =  max(dic, key=lambda k: dic[k])
        max_value = dic[max_key]
        candidates.append((max_value, node, max_key))
    
    candidates = sorted(candidates, reverse=True)[:10]
    combination_length = 3
    
    # Generate combinations
    combs = list(combinations(candidates, combination_length))
    
    # Print the result
    print(combs)


    class DSU:
        def __init__(self, nodes):
            self.parent = {node: node for node in nodes}
            
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                self.parent[root_x] = root_y
    
    def has_two_connected_components(nodes, connections):
        dsu = DSU(nodes)
        
        for edge in connections:
            dsu.union(edge[0], edge[1])
        
        components = defaultdict(int)
        for node in nodes:
            components[dsu.find(node)] += 1
        
        return components
    
    
    nodes = list(adj_dict.keys())
    
    for comb in tqdm.tqdm(combs):
        _, u0, v0 = comb[0]
        _, u1, v1 = comb[1]
        _, u2, v2 = comb[2]
        
        adj_dict[u0].remove(v0)
        adj_dict[u1].remove(v1)
        adj_dict[u2].remove(v2)
        adj_dict[v0].remove(u0)
        adj_dict[v1].remove(u1)
        adj_dict[v2].remove(u2)
        

        connections = []
        for node in nodes:
            for n_node in adj_dict[node]:
                connections.append((node, n_node))
    
        components = has_two_connected_components(nodes, connections)
        if len(components)==2: 
            print('yay')
            break
        
        adj_dict[u0].add(v0)
        adj_dict[u1].add(v1)
        adj_dict[u2].add(v2)
        adj_dict[v0].add(u0)
        adj_dict[v1].add(u1)
        adj_dict[v2].add(u2)


