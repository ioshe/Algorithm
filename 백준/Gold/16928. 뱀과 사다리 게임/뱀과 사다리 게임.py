#https://www.acmicpc.net/problem/16928
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
coordinates = dict(map(int, input().split()) for _ in range(n + m))
queue = deque([(1,0)])
visited = [False] * 100
while queue :
    x,count = queue.popleft()
    #print(x,count)
    if x+6 >= 100 :
        print(count+1)
        break
    for i in range(1,6+1):
        if not visited[x+i] :
            if x+i in coordinates:
                queue.append((coordinates[x+i],count+1))
            else :
                queue.append((x+i,count+1))
            visited[x+i] = True 