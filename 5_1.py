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

            
with open('inputs/input_5.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = list(map(int, lines[0].split(': ')[1].split()))
    
    seed_to_soil = []
    soil_to_fertilizer =[]
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    
    maps = {
        'seed-to-soil map:':seed_to_soil,
        'soil-to-fertilizer map:':soil_to_fertilizer,
        'fertilizer-to-water map:':fertilizer_to_water,
        'water-to-light map:':water_to_light,
        'light-to-temperature map:':light_to_temperature,
        'temperature-to-humidity map:':temperature_to_humidity,
        'humidity-to-location map:':humidity_to_location,
    }
    
    line_num = 2
    while line_num < len(lines):
        line = lines[line_num]
        if line in maps:
            ls = maps[line]
            line_num += 1
            while line_num < len(lines) and lines[line_num] != '':
                line = lines[line_num]
                dest, source, rge = list(map(int, line.split()))
                offset = dest-source
                start = source
                end = source + rge
                ls.append([start, end, offset])
                line_num += 1
        line_num+=1
    
    def find(ls, curr):
        for start, end, offset in ls:
            if start<=curr<=end:
                return curr + offset
        return curr
            
    ans = float('inf')
    
    for seed in seeds:
        
        soil = find(seed_to_soil, seed)
        fertilizer = find(soil_to_fertilizer, soil)
        water = find(fertilizer_to_water, fertilizer)
        light = find(water_to_light, water)
        temperature = find(light_to_temperature, light)
        humidity = find(temperature_to_humidity, temperature)
        location = find(humidity_to_location, humidity)
        ans = min(ans, location)
        
    print(ans)
        

            

