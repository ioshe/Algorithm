from sys import stdin

n,m = map(int,stdin.readline().split())
graph = [list(map(int,stdin.readline().split())) for i in range(n)]

for i in range(n):
    for j in range(m) :
        if graph[i][j] == 2 :
            start_x, start_y = i,j
            graph[i][j] = 0 
            break
direction = [(0,1),(0,-1),(1,0),(-1,0)]


def bfs(start) :
    queue = [start]
    while queue:
        i,j = queue.pop(0)
        for x,y in direction :
            nx,ny = x+i,y+j
            if 0<=nx<n and 0<=ny< m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[i][j]+1
                queue.extend([(nx,ny)])


bfs((start_x,start_y))

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            graph[i][j] = -1

for x,y in direction : 
    nx,ny = start_x+x,start_y+y
    if 0<=nx<n and 0<=ny< m and graph[nx][ny] != 0:
        graph[nx][ny] = 1
print("\n".join(" ".join(map(str,g)) for g in graph))