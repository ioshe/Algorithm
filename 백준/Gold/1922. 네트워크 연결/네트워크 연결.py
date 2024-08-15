import sys 
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
nums = list(map(lambda a : list(map(int,a.split())),sys.stdin.readlines()))
# a -> b : cost : c
graph = {i : [] for i in range(1,N+1)}
for u, v, weight in nums :
    graph[u].append((weight, v))
    graph[v].append((weight, u))

visited = [False] * (N + 1) 
min_heap = [(0,1)] # 가중치 정점
total_cost = 0

while min_heap :
    weight, u = heapq.heappop(min_heap)
    if visited[u] :
        continue
    visited[u] = True
    total_cost += weight

    for next_weight, v in graph[u] :
        if not visited[v] :
            heapq.heappush(min_heap,(next_weight,v))

print(total_cost)