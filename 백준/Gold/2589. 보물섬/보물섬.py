from collections import deque
import sys
input = sys.stdin.readline


def bfs(r,c):

    dist = [[0] * m for _ in range(n)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    visited[r][c] = True

    queue = deque()
    queue.append((r,c))

    while queue:

        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'L' and not visited[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                visited[nr][nc] = True
                queue.append((nr,nc))


    return max(map(max,dist))


n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            if 0 <= i - 1 and i + 1 < n:
                if board[i - 1][j] == 'L' and board[i + 1][j] == 'L':
                    continue
            if 0 < j - 1 and j + 1 < m:
                if board[i][j - 1] == 'L' and board[i][j - 1] == 'L':
                    continue
            answer = max(answer, bfs(i, j))

print(answer)