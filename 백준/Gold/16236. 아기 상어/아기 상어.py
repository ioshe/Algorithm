# https://www.acmicpc.net/problem/16236


# 이동 조건
## 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
## 거리가 가장 가까운 물고기를 먹으러 간다.
## 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
## 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고

# 종료 조건
## 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
import sys 
from collections import deque

def bfs(x,y) :
    visited = [[0 for i in range(N)] for i in range(N)] 
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cand = []
    queue = deque([(x,y)])
    visited[x][y] = 1

    while queue :
        i,j = queue.popleft()
        for idx in range(4) :
            nx,ny = i+dx[idx], j+dy[idx]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 :
				# 5. 간선은 상하 좌우지만 조건에 따라서 움직이기 때문에 조건을 상세하여야한다.
                if nums[x][y] > nums[nx][ny] and nums[nx][ny] != 0:
                    visited[nx][ny] = visited[i][j] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif nums[x][y] == nums[nx][ny] or nums[nx][ny] == 0:
                    visited[nx][ny] = visited[i][j] + 1
                    queue.append([nx,ny])
    cand.sort(key = lambda a : (a[0],a[1],a[2]))
    return cand[0] if cand else ""


MAX_SIZE = 6
N = int(sys.stdin.readline())
nums = list(map(lambda a : list(map(int,a.split())), sys.stdin.readlines()))

for i in range(N):
    for j in range(N):
        if nums[i][j] == 9:
            x,y = i,j
result = 0
cnt = 0
size = 2
cand = 1
while True :
    nums[x][y] = size
    cand = bfs(x,y)
    if not cand :
        break
    distance, xx, yy = cand[0],cand[1],cand[2]
    result += distance
    cnt += 1
    nums[x][y] = 0
    x,y = xx,yy
    if cnt == size:
        size += 1
        cnt = 0
print(result)
