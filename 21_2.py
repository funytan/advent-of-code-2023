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


with open('inputs/input_21.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]
    res = 0
    num_r = len(lines)
    num_c = len(lines[0])
    total_steps = 26501365
    # total_steps = 327 # 308013
    width = (total_steps//num_r)*2 + 1
    direcs = [(0,1),(0,-1),(1,0),(-1,0)]
    reachable = set()
    
    def search(node):
        stack = [node]
        visited = set([node])
        while stack:
            # print(stack)
            new_stack = []
            for r,c in stack:
                if r==65 and c == 65 or node in reachable:
                    return True
                for d in direcs:
                    n_r, n_c = r + d[0], c+ d[1]
                    if 0<=n_r<num_r and 0<=n_c<num_c and (n_r, n_c) not in visited and lines[n_r][n_c]!='#':
                        new_stack.append((n_r, n_c))
                        visited.add((n_r, n_c))
            stack = new_stack
        print(f"unreachable node: {node}")
        return False
                        
    
    row_empty = []
    unreachable = {(98, 9), (100, 63), (102, 99), (128, 8)}
    for r in range(num_r):
        count = 0
        for c in range(num_c):
            
            if lines[r][c] != '#':
                # can_reach = search((r,c))
                can_reach = (r,c) not in unreachable
                if can_reach:
                    count += 1
                    # reachable.add((r,c))
                else:
                    unreachable.add((r,c))
                    # 
        row_empty.append(count)
    
    # good method
    # left, right = 65, 65
    # dic = {-262:1}
    # for r in range(-261, 393):
    #     count = 0
    #     if r <= 65:
    #         left -=1
    #         right  +=1
    #     else:
    #         left += 1
    #         right -= 1
    #     for c in range(left, right+1):
    #         if lines[r%131][c%131] != '#' and (r+c) % 2==1 and (r%131,c%131) not in unreachable:
    #             count+=1
    #     dic[r] = count
    
    # print(sum([dic[k] for k in dic]))
    
    left, right = 65, 65
    upper_dic = {0:1}
    for r in range(1, 262):
        count = 0
        # if r <= 65:
        left -=1
        right  +=1
        # else:
        #     left += 1
        #     right -= 1
        for c in range(left, right+1):
            if lines[r%131][c%131] != '#' and (r+c) % 2==1 and (r%131,c%131) not in unreachable:
                count+=1
        upper_dic[r] = count
    
    
    
    for r in range(65-total_steps,66,1):
        num_grid = (r+(total_steps-65))//262
        mod_r = r%262
        res += upper_dic[mod_r] + num_grid*row_empty[r%131]*2
        # assert dic[r] == upper_dic[mod_r] + num_grid*row_empty[r%131]*2
    
    
    
    left, right = 65, 65
    lower_dic = {130:1}
    for r in range(129, -132,-1):
        count = 0
        left -=1
        right  +=1
        # print(r, left, right)
        for c in range(left, right+1):
            if lines[r%131][c%131] != '#' and (r+c) % 2==1 and (r%131,c%131) not in unreachable:
                count+=1
        lower_dic[r%262] = count
    
    for r in range(total_steps+65, 65, -1):
        num_grid = (total_steps+65-r)//262
        mod_r = r%262
        res += lower_dic[mod_r] + num_grid*row_empty[r%131]*2
        # assert dic[r] == lower_dic[mod_r] + num_grid*row_empty[r%131]*2
    
    # print(res)

    # 95144
    # small diamond
    
    # stack = [(65,65)]
    # steps = 327
    # curr_step = 0 
    # while curr_step<steps:
    #     new_stack = []
    #     for r,c in stack:
    #         for d in direcs:
    #             n_r, n_c = r+d[0], c+d[1]
    #             n_r_mod = n_r % 131
    #             n_c_mod = n_c % 131
    #             if (lines[n_r_mod][n_c_mod] == '.' or lines[n_r_mod][n_c_mod] == 'S'):
    #                 new_stack.append((n_r, n_c))
    #     new_stack = list(set(new_stack))
    #     stack = new_stack
    #     curr_step += 1
    # small_diamond = len(stack)

    
    # visited = set(stack)
    # correct = {}
    
    # for r in range(num_r):
    #     row = []
    #     for c in range(num_c):
    #         row.append(lines[r][c])
    #         if (r,c) in visited:
    #             row[-1] = 'O'
    #     correct[r] = row.count('O')

    # print(len(visited))
    
    
    
    # # for r in range(num_r):
    # #     row = []
    # #     for c in range(num_c):
    # #         row.append(lines[r][c])
    # #     print(''.join(row))
    
    
    
    
    # # small_half_width_plus = num_c//2+1
    # # start = None
    # # total_steps = 26501365
    
    # # count = 0 # count_odd
    # # for r in range(num_r):
    # #     for c in range(num_c):
    # #         if lines[r][c] != '#' and (r+c) % 2==1:
    # #             count+= 1
    # #         if lines[r][c] == 'S':
    # #             start = (r,c)
    # # width = (total_steps//num_r)*2 + 1
    # # within_grids = (width-1)**2//4 + (width-3)**2//4
        
    # small diamond
    
    # stack = [(65,65)]
    # steps = 65
    # curr_step = 0 
    # while curr_step<steps:
    #     new_stack = []
    #     for r,c in stack:
    #         for d in direcs:
    #             n_r, n_c = r+d[0], c+d[1]
    #             if 0<=n_r<num_r and 0<=n_c<num_c and (lines[n_r][n_c] == '.' or lines[n_r][n_c] == 'S'):
    #                 new_stack.append((n_r, n_c))
    #     new_stack = list(set(new_stack))
    #     stack = new_stack
    #     curr_step += 1
    # small_diamond = len(stack)
    
    # # res = 0
    # # res += within_grids * count
    # # res += (width-1) * count * 2
    # # res -= count-small_diamond
    
    # visited = set(stack)
    # correct = {}
    
    # for r in range(num_r):
    #     row = []
    #     for c in range(num_c):
    #         row.append(lines[r][c])
    #         if (r,c) in visited:
    #             row[-1] = 'O'
    #     correct[r] = row.count('O')

    
    
    
    # 26501365%131 = 65
    # 26501365//131 = 202300
    
    # 620184910321777 low (without small diamond)
    # 620184910321812 incorrect
    # 621658246450148 incorrect
    # 621658246450149 incorrect
    # 621494544480948 incorrect
   #  621494544278648 correct!!!
    # 623131545763648 high