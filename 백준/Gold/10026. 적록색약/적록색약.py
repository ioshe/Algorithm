# https://www.acmicpc.net/problem/10026
from sys import stdin
from collections import deque

def bfs(i,j,blind,visited) :
    
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    if visited[i][j] == False :
        queue = deque([(i,j)])
        while queue :
            x,y = queue.popleft()
            for x_p,y_p in (move) :
                n_x,n_y = x+x_p,y+y_p
                if 0<=n_x<n and 0 <=n_y<n and not visited[n_x][n_y] :
                    if blind and rgb[i][j] in ['R','G'] and rgb[n_x][n_y] in ['R','G']  :
                        # blind 인 사람들의 방문 기준
                        visited[n_x][n_y] = True
                        queue.append((n_x,n_y))
                        continue
                    if rgb[i][j] == rgb[n_x][n_y]  :
                        visited[n_x][n_y] = True
                        queue.append((n_x,n_y))
        return 1
    return 0

def color_for(blind) :
    count = 0
    visited = [[False for i in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            count +=bfs(i,j,blind,visited)
            # print(visited)
    return count

n = int(stdin.readline())
rgb = list(map(lambda a: ' '.join(a).split(),stdin.read().splitlines()))

print(color_for(False), color_for(True))






# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
