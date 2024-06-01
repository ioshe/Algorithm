from sys import stdin 
from heapq import heappush,heappop,heapify

n,m = map(int,stdin.readline().split()) 
nums = list(map(int,stdin.readline().split()))

heapify(nums)

for _ in range(m) : 
    a = heappop(nums) 
    b = heappop(nums) 
    temp = a+b 
    heappush(nums,temp) 
    heappush(nums,temp)

print(sum(nums))