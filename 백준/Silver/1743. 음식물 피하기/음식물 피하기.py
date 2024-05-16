# https://www.acmicpc.net/problem/1743
from sys import stdin
from collections import deque
def dfs(x,y) :
    global grpah,N,M
    queue = deque([(x,y)])
    count = 1
    while queue :
        i,j = queue.popleft()
        for px,py in ([(0,1),(0,-1),(1,0),(-1,0)]) :
            nx,ny = i + px, j + py 
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
    return count 

N,M,K = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())), stdin.readlines()))
#  세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100)
graph = [[0 for i in range(M)] for j in range(N)]

for num in nums :
    graph[num[0]-1][num[1]-1] = 1

count = 0
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 :
            graph[i][j] = 0 
            count = max(dfs(i,j),count)

print(count)