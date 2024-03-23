from sys import stdin

def dfs(x,y,count,plus) :
    global visited, graph, max_count
    if count == 4 :
        max_count = plus if max_count < plus else max_count
        return  
    for px,py in [(0,1),(0,-1),(1,0),(-1,0)] :
        nx, ny = x+px, y+py
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False :
            visited[nx][ny] = True
            dfs(nx,ny,count + 1, plus + graph[nx][ny])
            visited[nx][ny] = False
    return 

def find_T(i,j) :
    global graph, max_count
    dy = [0, 1, 0, -1] 
    dx = [1, 0, -1, 0]
    for x in range(4):  # 4방향을 기준으로 하여 'ㅗ', 'ㅜ', 'ㅏ', 'ㅓ' 모양 탐색
        sum = graph[i][j]  # 중심점의 값부터 시작
        for dir in range(4):
            if dir == x:  # 현재 방향을 제외
                continue
            nx = i + dy[dir]
            ny = j + dx[dir]
            if 0 <= nx < n and 0 <= ny < m:
                sum += graph[nx][ny]
        max_count = sum if max_count < sum else max_count

n,m = map(int,stdin.readline().split())
graph = list(map(lambda a : list(map(int,a.split())), stdin.read().splitlines()))
visited = [[False for _ in range(m)] for i in range(n)]
max_count = 0

for i in range(n) : 
    for j in range(m) :
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        find_T(i,j)
print(max_count)