import heapq

from sys import stdin
from collections import defaultdict

def dijkstra(N,graph, start ,end):
    priority_queue = []
    heapq.heappush(priority_queue, (0,start))
    
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 더 짧은 경로가 있으면 스킵
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances[end]


N = int(stdin.readline())
M = int(stdin.readline())

graph = [dict() for _ in range(N + 1)]
for i in range(M):
    start, end, cost = map(int, input().split())
    # 간선 추가
    if end not in graph[start] or graph[start][end] > cost:
        graph[start][end] = cost

start, end = map(int,stdin.readline().split())

print(dijkstra(N,graph,start,end))
