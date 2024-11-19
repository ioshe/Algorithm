# https://www.acmicpc.net/problem/1325

# A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다
# A를 해킹했을 때는 B를 해킹할 수 없다 
# 따라서 방향성은 B -> A 가 된다.

from sys import stdin
from collections import deque

N,M = map(int, stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))

graph = [[] for i in range(N + 1)]
for i,j in nums :
    graph[j].append(i)

def bfs(i) :
    queue = deque([i])
    visited = [False for _ in range(N+1)]
    visited[i] = True
    cnt = 1
    while queue :
        current = queue.popleft()
        for next in graph[current] :
            if not visited[next] :
                visited[next] = True
                queue.append(next)
                cnt += 1
    return cnt

result = []
max_cnt = 0
for i in range(1,N+1) :
    tmp = bfs(i) 
    if max_cnt == tmp : 
        result.append(i) 
    elif max_cnt < tmp : 
        max_cnt = tmp 
        result = []
        result.append(i)
print(*result)