# https://www.acmicpc.net/problem/16234


'''
2 20 50
50 30
20 40
'''

from sys import stdin
from collections import deque

moving = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(n,i,j,visited,graph,L,R):
    territory = [(i,j)]
    queue = deque([(i,j)])
    visited[i][j] = True
    population_sum = graph[i][j]
    count = 1
    
    while queue :
        x,y = queue.popleft()
        for mx,my in moving:
            nx, ny = mx + x, my + y
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                diff = abs(graph[x][y] - graph[nx][ny])
                if L <= diff <= R:
                    queue.append((nx,ny))
                    territory.append((nx,ny))
                    visited[nx][ny] = True
                    population_sum += graph[nx][ny]
                    count += 1
                    
    
    if count > 1:
        new_population = population_sum // count
        for x,y in territory:
           graph[x][y] = new_population
        return True
    else :
        return False    
    
n, L, R = map(int,stdin.readline().split())
graph = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

result = False
count = 0

while True:
    visited = [[False] * n for _ in range(n)]
        
    for i in range(n):
        for j in range(n):
            if not(visited[i][j]) :
                result += bfs(n,i,j,visited,graph,L,R)
    if result:
        count += 1
        result = False
    else:
        break
                
# print("\n".join(" ".join(map(str,g)) for g in graph))
print(count)