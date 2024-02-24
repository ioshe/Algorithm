# https://www.acmicpc.net/problem/1417

from sys import stdin
import heapq
n = list(map(lambda x : -x,map(int,stdin.read().splitlines()[1:])))

target = n.pop(0)
count  = 0
if n :
    heapq.heapify(n)
    temp = heapq.heappop(n)
    while temp <= target :
        # print(n)
        # print(temp)
        temp += 1
        target -=1 
        heapq.heappush(n,temp)
        temp = heapq.heappop(n)
        count += 1

print(count)