# https://www.acmicpc.net/problem/2210
from sys import stdin
graph = [list(map(int,stdin.readline().split())) for i in range(5)]
visited = []
result = set()
def dfs() :
    global graph
    for i in range(len(graph)) :
        for j in range(len(graph[i])) :
            if graph[i][j] not in visited :
                search(i,j)
                
def search(i,j) :
    if len(visited) >= 6 :
        result.add(tuple(visited))
        return
    
    if i > 0:
        visited.append(graph[i][j])
        search(i-1,j)
        visited.pop()
    if i < 4 :
        visited.append(graph[i][j])
        search(i+1,j)
        visited.pop()
    if j > 0 :
        visited.append(graph[i][j])
        search(i,j-1)
        visited.pop()
    if j < 4 :
        visited.append(graph[i][j])
        search(i,j+1)
        visited.pop()
    
dfs() 
print(len(result))


