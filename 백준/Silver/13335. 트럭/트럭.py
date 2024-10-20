# https://www.acmicpc.net/problem/13335

from sys import stdin
from collections import deque

N,W,L = map(int,stdin.readline().split())
queue = deque(list(map(int,stdin.readline().split())))

weight = 0
on_bridge = deque([])
cnt = 0

while queue or on_bridge :
    if on_bridge and on_bridge[0][0] == 0 : 
        weight -= on_bridge[0][1]
        on_bridge.popleft()

    if queue and queue[0] + weight <= L :
        truck = queue.popleft()
        on_bridge.append([ W ,truck ])
        weight += truck
    
    for i in range(len(on_bridge)) :
        on_bridge[i][0] -= 1
    # print(on_bridge)
    cnt += 1

print(cnt)