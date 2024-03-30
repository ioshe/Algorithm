# https://www.acmicpc.net/problem/2583

from sys import stdin
from collections import deque

def bfs(i,j) :
    global graph,M,N
    count = 1
    queue = deque([(i,j)])
    while queue :
        x,y = queue.popleft()
        for px,py in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx,ny = px+x, py+y
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 0 :
                count += 1
                graph[nx][ny] = 1
                queue.append((nx,ny))
    return count


M,N,K = map(int,stdin.readline().split())
locations = list(map(lambda a : list(map(int,a.split())),stdin.read().splitlines()))
graph = [[0 for i in range(N)] for j in range(M)]

for x,y,lx,ly in locations :
    for i in range(y,ly) :
        for j in range(x,lx) :
            graph[i][j] = 1

result = []

for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 0 :
            graph[i][j] = 1
            result.append(bfs(i,j))
result.sort()
print(len(result))
print(" ".join(map(str,result)))