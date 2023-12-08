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
from bisect import bisect_left
from functools import lru_cache

dic = {
       'zero':0,
       'one':1,
       'two':2,
       'three':3,
       'four':4,
       'five':5,
       'six':6,
       'seven':7,
       'eight':8,
       'nine':9, 
}

reverse_dic = {key[::-1]:dic[key] for key in dic}
            
with open('inputs/input_1.txt', 'r') as f:
    curr_sum = 0
    lines = f.readlines()
    for line in lines:
        inp = line.strip()
        for i, ch in enumerate(inp):
            if '0'<=ch<='9':
                first_digit = int(ch)
                first_digit_idx = i
                break
        for i, ch in enumerate(inp[::-1]):
            if '0'<=ch<='9':
                second_digit = int(ch)
                second_digit_idx = len(inp)-i-1
                break
        first_word = None
        first_word_idx = None
        second_word = None
        second_word_idx = None
        for word in dic:
            idx = inp.find(word)
            if idx == -1:
                continue
            if first_word_idx is None or idx < first_word_idx:
                first_word = dic[word]
                first_word_idx = idx
        for word in reverse_dic:
            idx = inp[::-1].find(word)
            if idx == -1:
                continue
            idx = len(inp) - idx - 1
            if second_word_idx is None or idx > second_word_idx:
                second_word = reverse_dic[word]
                second_word_idx = idx
        
        if first_word is None or first_digit_idx < first_word_idx:
            first = first_digit
        else:
            first = first_word
        
        if second_word is None or second_digit_idx > second_word_idx:
            second = second_digit
        else:
            second = second_word
        
        curr_sum += first*10 + second
        
        print(curr_sum)