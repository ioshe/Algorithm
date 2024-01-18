# https://www.acmicpc.net/problem/1260
from sys import stdin

def bfs(v,graph,visited) :
    queue = [v]
    while queue :
        temp= queue.pop(0)
        if temp not in visited :
            visited.append(temp)
            queue.extend(i for i in graph[temp] if i not in visited)
    return visited

def dfs(v,graph,visited) :
    for i in graph[v] :
        if i not in visited :
            visited.append(i) 
            dfs(i,graph,visited)
    return visited
    
n,m,v = map(int,stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}  # 모든 정점에 대해 빈 리스트 초기화

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for index in graph:
    graph[index].sort()

#print(graph)
print(" ".join(map(str,dfs(v,graph,[v]))))
print(" ".join(map(str,bfs(v,graph,[]))))