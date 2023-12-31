#https://www.acmicpc.net/problem/2075
from sys import stdin
import heapq
n=int(input())
heap = []
for i in range(n) :
    nums = list(map(int,stdin.readline().split()))
    if not heap :
        for num in nums : 
            heapq.heappush(heap,num) 
    else :
        for num in nums :
            if heap[0] < num :
                heapq.heappush(heap,num)
                heapq.heappop(heap)
print(heap[0])