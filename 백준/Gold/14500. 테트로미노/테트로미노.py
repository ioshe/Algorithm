from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
highest_value = max(map(max, graph))    # 보드에서 가장 큰 값
max_count = 0

def dfs(x, y, count, score):
    global max_count, graph
    # 남은 칸으로 최대 점수를 얻어도 현재 max_score보다 작으면 탐색 중지
    if max_count > score + highest_value * (4 - count):
        return
    if count == 4:
        max_count = max(max_count, score)
        return
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            temp = graph[nx][ny]
            if count == 2:  # 'ㅗ' 모양 테트로미노 처리
                visited[nx][ny] = True
                dfs(x, y, count + 1, score + temp)
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, score + temp)
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = False

print(max_count)
