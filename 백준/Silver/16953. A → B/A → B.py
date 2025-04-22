# https://www.acmicpc.net/problem/16953

from collections import deque

A,B = map(int, input().split())

queue = deque([(A, 1)])
visited = set()
result = float('inf')
while queue:
    num, cnt = queue.popleft()
    if num == B:
        result = min(result, cnt)
        break
    if num > B:
        continue

    if num * 2 not in visited:
        queue.append((num * 2, cnt + 1))
        visited.add(num * 2)
    
    if num * 10 + 1 not in visited:
        queue.append((num * 10 + 1, cnt + 1))
        visited.add(num * 10 + 1)

print(result if result != float('inf') else -1)