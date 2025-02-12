# https://www.acmicpc.net/problem/16948

from sys import stdin
from collections import deque

n = int(stdin.readline())
r1,c1,r2,c2 = map(int,stdin.readline().split())

moving = [(-2,-1), (-2,+1), (0,-2), (0,+2), (+2,-1), (+2,+1)]

queue = deque([(r1,c1)])

visited = [[0 for i in range(n)] for j in range(n)]
visited[r1][c1] = 1

while queue :
    x, y = queue.popleft()
    if r2 == x and c2 == y:
        print(visited[x][y] - 1)
        exit(0)
    for dx, dy in moving:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1  # 방문 표시
            queue.append((nx, ny))

# print("\n".join([" ".join(list(map(str,i))) for i in visited]))
if visited[r2][c2] == 0:
    print(-1)
else:    
    print(visited[r2][c2])
