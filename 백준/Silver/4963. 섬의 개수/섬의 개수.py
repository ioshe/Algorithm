from sys import stdin
from collections import deque


def bfs(graph,start) :
    global n,m
    queue= deque([start])

    while queue :
        x,y = queue.popleft()
        for (px, py) in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]:
            nx,ny = px+x,py+y
            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny]=0
                queue.append((nx,ny))


result = []
while True :
    n,m = map(int,stdin.readline().split())
    if n==0 and m == 0:
        break
    graph = [list(map(int,stdin.readline().split())) for i in range(m)]
    count = 0
    for i in range(m) :
        for j in range(n) :
            if graph[i][j] == 1 :
                count += 1
                graph[i][j] = 0
                bfs(graph,(i,j))
    result.append(count)

print("\n".join(map(str,result)))