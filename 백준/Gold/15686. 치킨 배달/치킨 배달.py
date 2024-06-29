# https://www.acmicpc.net/problem/15686

from sys import stdin
from itertools import combinations

def calculate_distance(home_position,chicken_position) : 
    total_distance = 0
    for hx,hy in home_position :
        min_distance = float('inf')
        for sx,sy in chicken_position : 
            min_distance = min(min_distance,abs(hx - sx) + abs(hy - sy))
        total_distance += min_distance
    return total_distance

N,m = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

result = []
home_position = []
chicken_position = {}

for i in range(N) :
    for j in range(N) : 
        if nums[i][j] == 1 :
            home_position.append((i,j))
            continue
        if nums[i][j] == 2 :
            chicken_position[(i,j)] = []
            continue

min_chicken_distance = float('inf')
for cp in combinations(chicken_position,m) :
    current_distance = calculate_distance(home_position,cp)
    min_chicken_distance = min(min_chicken_distance,current_distance)

print(min_chicken_distance)
    