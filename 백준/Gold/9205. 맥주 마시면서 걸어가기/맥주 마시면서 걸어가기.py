# https://www.acmicpc.net/problem/9205

from sys import stdin
from collections import deque

def can_reach_festival(n, locations):
    queue = deque([0]) # 상근이 집
    visited = [False] * (n + 2)
    visited[0] = True
    
    while queue:
        current = queue.popleft()
        cx, cy = locations[current]
        
        if current == n + 1 :
            return "happy"
        
        for i in range(n+2):
            if not visited[i]:
                nx, ny = locations[i]
                if abs(cx - nx) + abs(cy - ny) <= 1000:
                    queue.append(i)
                    visited[i] = True
        
    return "sad"
    
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    locations = [tuple(map(int, stdin.readline().split())) for _ in range(n + 2)]
    print(can_reach_festival(n, locations))