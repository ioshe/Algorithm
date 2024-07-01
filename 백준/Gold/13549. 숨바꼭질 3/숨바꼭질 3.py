# https://www.acmicpc.net/problem/13549

from collections import deque

N,K = map(int,input().split())
# 수빈이 N, 동생이 있는 위치 K

# 1초 후에 X-1, X+1 순간이동 하는 경우 0초 후에 2*X
queue = deque([(N,0)])
MAX_POSITION = 100000
visited = [float('inf') for i in range(MAX_POSITION + 1)]

def isValid(count) :
    global MAX_POSITION
    return 0 <= count <= MAX_POSITION

if (N >= K) :
    minTime = N - K;	# -1 칸씩 n-k 번 이동하는 한 가지
else :    
    while queue :
        num, count = queue.popleft()

        np1 = num + 1
        if isValid(np1) and visited[np1] > count + 1 :
            visited[np1] = count + 1
            queue.append((np1,visited[np1]))

        np2 = num - 1
        if isValid(np2) and visited[np2] > count + 1 :
            visited[np2] = count + 1
            queue.append((np2,visited[np2]))

        np3 = num * 2
        if isValid(np3) and visited[np3] > count :
            visited[np3] = count
            queue.append((np3,visited[np3]))
    minTime = visited[K]
print(minTime)