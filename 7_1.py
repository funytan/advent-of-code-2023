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


def determine_rank(cards):
    cards = sorted(cards)
    prev = cards[0]
    num = 1
    ls = []
    for card in cards[1:]:
        if card != prev:
            ls.append((prev, num))
            prev = card
            num = 1
        else:
            num += 1
    ls.append((prev, num))
    nums = [item[1] for item in ls]
    
    if 5 in nums:
        return 1
    elif 4 in nums:
        return 2
    elif 3 in nums and 2 in nums:
        return 3
    elif 3 in nums:
        return 4
    elif nums.count(2) == 2:
        return 5
    elif nums.count(2) == 1:
        return 6
    elif len(nums) == 5:
        return 7
    assert False
    
card_map = {
    'A': 1,
    'K': 2, 
    'Q': 3,
    'J': 4,
    'T': 5,
    '9': 6, 
    '8': 7, 
    '7': 8,
    '6': 9,
    '5': 10,
    '4': 11,
    '3': 12,
    '2': 13,
}

def custom_sort(item):
    rank, cards, bid = item
    val = 0
    for card in cards:
        val *= 13
        val += card_map[card]
    return (rank, val, bid)
            
            
with open('inputs/input_7.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    hands = []
    for idx, line in enumerate(lines):
        cards, bid = line.split()
        bid = int(bid)
        hands.append((determine_rank(cards), cards, bid))

    hands = sorted(hands, key=custom_sort)
    total = len(hands)
    res = 0
    for hand in hands:
        rank, cards, bid = hand
        res += bid*total
        total -= 1
    print(res)
