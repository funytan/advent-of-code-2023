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

import sys
sys.setrecursionlimit(10000)


with open('inputs/input_19.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    workflows = {}
    
    for idx, line in enumerate(lines):
        if len(line.strip()) == 0:
            break
        workflow, rules = line.split('{')
        rules = rules[:-1].split(',')
        rule_ls = []
        for rule in rules:
            if ':' not in rule:
                rule_ls.append((None, None, None, rule))
            else:
                part = rule[0]
                is_greater = rule[1] == '>'
                num = int(rule.split(':')[0][2:])
                n_workflow = rule.split(':')[1]
                rule_ls.append((part, is_greater, num, n_workflow))
                
        workflows[workflow] = rule_ls
        
    for i, line in enumerate(lines[idx+1:], idx+1): 
        line = line[1:-1]
        parts = line.split(',')
        parts_dict = {part[0]:int(part[2:]) for part in parts}
        curr_workflow = 'in'
        while curr_workflow != 'A' and curr_workflow!='R':
            for rule in workflows[curr_workflow]:
                part, is_greater, num, n_workflow = rule
                if part is None:
                    curr_workflow = n_workflow
                    break
                else:
                    if is_greater:
                        if parts_dict[part] > num:
                            curr_workflow = n_workflow
                            break
                    else:
                        if parts_dict[part] < num:
                            curr_workflow = n_workflow
                            break
                
        if curr_workflow == 'A':
            res += sum([parts_dict[part] for part in parts_dict])
    
    print(res)
        
    
    # print(len(dug))
    # print(res)
    # 127 93 161 93
    #10 3 17 3