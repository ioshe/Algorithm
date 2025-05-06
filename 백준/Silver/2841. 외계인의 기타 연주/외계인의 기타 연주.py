# https://www.acmicpc.net/problem/2841

from sys import stdin
from heapq import heapify, heappop, heappush

N,P = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

result = 0
queue = {}

for line_num, flat in nums:
    if line_num not in queue:
        queue[line_num] = [-flat]
        heapify(queue[line_num])
        result += 1
        continue

    while queue[line_num] and -queue[line_num][0] > flat:
        heappop(queue[line_num])
        result += 1
    
    if queue[line_num] and -queue[line_num][0] == flat:
        continue 

    heappush(queue[line_num], -flat)
    result += 1

print(result)