# https://www.acmicpc.net/problem/1753

'''
input : 
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

output : 
0
2
3
7
INF
'''

from sys import stdin
import heapq
V,E = map(int,stdin.readline().split())
K = int(stdin.readline())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
# u,v,w
# 에서 v로 가는 가중치 w인 간선이 존재한다.
# u 와 v는 다르다. w 는 10 이하의 자연수이다. 
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있다.
# 정점이 2만개 한계, 간선이 30만개
def bfs(graph,K,V,result) :
    queue = [(0,K)] 
    while queue :
        current_distance,u = heapq.heappop(queue)
        if result[u-1] < current_distance : 
            continue
        for u,weight in graph[u] :
            distance = current_distance + weight
            if distance < result[u-1] :
                result[u-1] = distance
                heapq.heappush(queue,(distance,u)) 

graph = [[] for _ in range(V + 1)]
for (u,b,w) in nums :
    graph[u].append((b,w))
result = [float('inf') for i in range(V)]
result[K-1] = 0
bfs(graph,K,V,result)
print("\n".join(map(lambda a : 'INF' if a == float('inf') else str(a) ,result)))