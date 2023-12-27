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
        
    
    def process_ranges(mini, maxi, num, is_greater):
        assert mini< maxi
        if is_greater:
            if num < maxi:
                if mini > num:
                    return (mini, maxi), None
                else:
                    return (num+1, maxi), (mini, num)
            else:
                return None, (mini, maxi)
        else:
            if mini < num:
                if maxi < num:
                    return (mini, maxi), None
                else:
                    return (mini, num-1), (num, maxi)
            else:
                return None, (mini, maxi)
            
    # def consolidate_range_len(ranges):
    #     ranges = sorted(ranges)
    #     range_len = 0
    #     prev_start = ranges[0]
    #     prev_end = ranges[1]
    #     for r in ranges[1:]:
    #         s, e = r
    #         if s <= prev_end:
    #             prev_end = e
    #         else:
    #             range_len += prev_end - prev_start + 1
    #             prev_start = s
    #             prev_end = e
    #     range_len += prev_end - prev_start + 1
    #     return range_len
    
    def modify_ranges(part, x_range, m_range, a_range, s_range, mini, maxi):
        assert mini< maxi
        if part == 'x':
            x_range = (mini, maxi)
        elif part == 'm':
            m_range = (mini, maxi)
        elif part == 'a':
            a_range = (mini, maxi)
        else:
            s_range = (mini, maxi)
        return x_range, m_range, a_range, s_range
             
    
    stack = [['in', (1,4000), (1,4000), (1,4000), (1,4000)]]
    x_ranges = []
    m_ranges = []
    a_ranges = []
    s_ranges = []
    while stack:
        # print(stack)
        workflow, x_range, m_range, a_range, s_range = stack.pop()
        if workflow == 'A':
            res += (x_range[1] - x_range[0]+1)*(m_range[1] - m_range[0]+1)*(a_range[1] - a_range[0]+1)*(s_range[1] - s_range[0]+1)
            # print(x_range, m_range, a_range, s_range)
            continue
        if workflow == 'R':
            continue
        for rule in workflows[workflow]:
            part, is_greater, num, n_workflow = rule
            if not part:
                stack.append([n_workflow, x_range, m_range, a_range, s_range])
            else:
                curr = {
                    'x': x_range,
                    'm': m_range,
                    'a': a_range,
                    's': s_range,
                }
                part_mini = curr[part][0]
                part_maxi = curr[part][1]
                passed, not_passed = process_ranges(part_mini, part_maxi, num, is_greater)
                
                # print(passed, not_passed, part, num, is_greater)
                if passed is not None:
                    x_range_new, m_range_new, a_range_new, s_range_new = modify_ranges(
                        part = part,
                        x_range = x_range,
                        m_range = m_range,
                        a_range = a_range,
                        s_range = s_range,
                        mini = passed[0],
                        maxi = passed[1]
                    )
                    stack.append([n_workflow, x_range_new, m_range_new, a_range_new, s_range_new])
                if not_passed is not None: # modify existing range
                    x_range, m_range, a_range, s_range = modify_ranges(
                        part = part,
                        x_range = x_range,
                        m_range = m_range,
                        a_range = a_range,
                        s_range = s_range,
                        mini = not_passed[0],
                        maxi = not_passed[1]
                    )

                else:
                    break
    
    print(res)
        
    
    # print(len(dug))
    # print(res)
    # 127 93 161 93
    #10 3 17 3