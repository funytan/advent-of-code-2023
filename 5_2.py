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
                ls.append([start, end-1, offset])
                line_num += 1
        line_num+=1
        
    def check(ls):
        prev_end = -float('inf')
        for start, end in ls:
            if start <= prev_end:
                return False
            prev_end = end
        return True
        
    
    def find(ls, seed_pair, view=False):
        ls = sorted(ls)
        first_seed, last_seed = seed_pair
        first_seed_pass = False
        res = []
        curr = first_seed
        for start, end, offset in ls:
            # print(curr, start, end)
            if last_seed < start:
                break
            if curr > end: continue
            if curr < start:
                res.append((curr, start-1))
            curr = max(start, curr)
            if last_seed <= end:
                res.append((curr+offset, last_seed+offset))
                # if view:
                #     print(res, seed_pair)
                return res
            else:
                res.append((curr+offset, end+offset))
                curr = end+1
        res.append((curr, last_seed))
        return res
            
    ans = float('inf')
    seed_pairs = []
    
    for i in range(0,len(seeds),2):
        seed_pairs.append([seeds[i], seeds[i] + seeds[i+1]-1])
    
    ans = []
    for pair in seed_pairs:
        ans += find(seed_to_soil, pair)
    soils = sorted(ans)
    # print(soils, check(soils))
    print(check(soils))

    ans = []
    for pair in soils:
        ans += find(soil_to_fertilizer, pair)
    fertilizers = sorted(ans)
    # print(fertilizers, check(fertilizers))
    print(check(fertilizers))

    ans = []
    for pair in fertilizers:
        ans += find(fertilizer_to_water, pair)
    waters = sorted(ans)
    # print(waters, check(waters))
    print(check(waters))
    
    ans = []
    for pair in waters:
        ans += find(water_to_light, pair)
    lights = sorted(ans)
    # print(lights, check(lights))
    print(check(lights))

    ans = []
    for pair in lights:
        ans += find(light_to_temperature, pair)
    temperatures = sorted(ans)
    # print(temperatures, check(temperatures))    
    print(check(temperatures))
    
    ans = []
    for pair in temperatures:
        ans += find(temperature_to_humidity, pair, view=True)
    humidities = sorted(ans)
    print(check(humidities))
    # print(check(humidities))
    
    ans = []
    for pair in humidities:
        ans += find(humidity_to_location, pair)
    locations = sorted(ans)
    print(check(locations))
        
    print(sorted(locations)[0][0])
        

            

