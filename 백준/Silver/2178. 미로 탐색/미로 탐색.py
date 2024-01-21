from collections import deque
from sys import stdin
n,m = map(int,stdin.readline().split())
text = stdin.read().splitlines()
graph = [list(map(int,' '.join(line).split(' '))) for line in text]
queue = deque([(0,0)])
while queue :
    (i,j) = queue.popleft()
    for (x,y) in ([0,1],[0,-1],[1,0],[-1,0]) :
        nx,ny = x+i,y+j
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 :
            graph[nx][ny] = int(graph[i][j])+1
            queue.append((nx, ny))
print(graph[-1][-1])