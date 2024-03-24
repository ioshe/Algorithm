#https://www.acmicpc.net/problem/7569

from sys import stdin
from collections import deque
M,N = map(int,stdin.readline().split())
graph = list(map(lambda a : list(map(int,a.split())), stdin.read().splitlines()))
turn = 1

def grow_tomato(queue) :
    global graph
    while queue :
        i,j = queue.popleft()
        for px, py in [(0,1),(1,0),(-1,0),(0,-1)] :
            nx,ny = i+px, j+py
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0 :
                graph[nx][ny] = graph[i][j] + 1
                queue.append((nx,ny))

queue = deque()
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 :
            queue.append((i,j))

grow_tomato(queue)

# 모든 토마토가 익는 데 필요한 최소 일수 계산
answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:  # 익지 않은 토마토가 있으면
            print(-1)
            exit(0)
        answer = max(answer, graph[i][j])

# 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력
if answer == 1:
    print(0)
else:
    print(answer - 1)  # 최소 일수는 최대값에서 1을 빼서 계산