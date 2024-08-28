# https://www.acmicpc.net/problem/1453

from sys import stdin

n = int(stdin.readline())
visited = [False for i in range(101)]
count = 0
for i in list(map(int,stdin.readline().split())) :
    if not(visited[i]) :
        visited[i] = True
    else :
        count +=1 
print(count)