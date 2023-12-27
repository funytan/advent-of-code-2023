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


with open('inputs/input_20.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    res = 0
    ff_state = {}
    con_state = {}
    output_dict = defaultdict(list)
    out_dict = {}
    circuit_to_type = {}
    out_change_frequency = defaultdict(list)
    prev_state = {}
    
    for line in lines:
        circuit, out = [item.strip() for item in line.split('->')]
        out_ls = out.split(', ')
        t = circuit[0]
        if circuit[0] == 'b':
            circuit_to_type[circuit] = 'b'
        else:
            circuit = circuit[1:]
        if t == '%':
            ff_state[circuit] = 0
            circuit_to_type[circuit] = 'ff'
        elif t=='&':
            con_state[circuit] = None
            circuit_to_type[circuit] = 'con'
        for output in out_ls:
            output_dict[output].append(circuit)
        out_dict[circuit] = out_ls
        if circuit_to_type[circuit] == 'ff':
            prev_state[circuit] = 0
        else:
            prev_state[circuit] = 1
        
    for circuit in con_state:
        con_state[circuit] = {}
        for inp in output_dict[circuit]:
            con_state[circuit][inp] = 0

    res_low = 0
    res_high = 0
    impt_nodes = set([
        'vb', 'tf', 'tx', 'sc', 'cc', 'rj', 'vh',
        'tn', 'hc', 'zn', 'gf', 'lt', 'qf', 'ls', 'fv', 
        'hj', 'hr', 'pp', 'nc', 'lk', 'rk', 'rv', 'bp',
        'rb', 'mf', 'xv', 'jz', 'br', 'kh', 'lj'
        ])
    
        
    def simulate(i):
        num_low = 0
        num_high = 0
        stack = [('broadcaster', 0, None)] # circuit and signal received
        check_rx = False
        state = {}
        while len(stack) > 0:
            new_stack = []
            for item in stack:
                c, s, f = item
                # if c == 'rx' and s == 0:
                #     print('here')
                #     check_rx = True
                #     break
                # if c == 'jq':
                #     print(i, con_state[c])
                if s == 0:
                    num_low += 1
                else:
                    num_high += 1
                if f in ('ck', 'kz', 'hh', 'ns') and s==1:
                    print(f, i)
                
                if f not in state:
                    state[f] = s
                else:
                    state[f] = s
                    # assert state[f] == s, f
                if c not in circuit_to_type:
                    continue
                elif circuit_to_type[c] == 'b':
                    for out_c in out_dict[c]:
                        new_stack.append([out_c, s, c])
                elif circuit_to_type[c] == 'ff':
                    if s == 0:
                        if ff_state[c] == 0:
                            ff_state[c] = 1
                        else:
                            ff_state[c] = 0
                        for out_c in out_dict[c]:
                            new_stack.append([out_c, ff_state[c], c])
                    # do nothiing
                else:
                    con_state[c][f] = s
                    if all([con_state[c][inp]==1 for inp in con_state[c]]):
                        out_s = 0
                    else:
                        out_s = 1
                    for out_c in out_dict[c]:
                        new_stack.append([out_c, out_s, c])
            stack = new_stack
        return num_low, num_high, state
    
    for i in range(1, 1000000):
        num_low, num_high, state = simulate(i)
        for key in state:
            if key is not None and state[key] != prev_state[key]:
                prev_state[key] = state[key]
                if len(out_change_frequency[key]) > 0:
                    prev_i = out_change_frequency[key][-1][0]
                    out_change_frequency[key].append((i, prev_state[key], i- prev_i))
                else:
                    out_change_frequency[key].append((i, prev_state[key], None))
        res_low += num_low
        res_high += num_high
        
    cycle_dict = []
    final = {}
    for key in out_change_frequency:
        if key == 'broadcaster':
            continue
        ls = out_change_frequency[key]
        if len(ls) < 4:
            continue
        final[key] = out_change_frequency[key]
        cycle_len = ls[-1][0] - ls[-3][0]
        # assert cycle_len == ls[-2][0] - ls[-4][0]
    
    # print(i)
    # print(res_low, res_high, res_low*res_high)
        
    