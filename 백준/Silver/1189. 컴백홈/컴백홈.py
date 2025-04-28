from sys import stdin

R, C, K = map(int, stdin.readline().split())
dis = [list(stdin.readline().strip()) for _ in range(R)]

moving = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(x, y, route):
    global dis, R, C, K, moving

    if route > K:
        return 0
    if route == K and x == C - 1 and y == 0:
        return 1
    
    cnt = 0
    for ix, iy in moving:
        nx, ny = x + ix, y + iy 
        if 0 <= nx < C and 0 <= ny < R and dis[ny][nx] != "T":
            dis[ny][nx] = "T"
            cnt += dfs(nx, ny, route + 1)
            dis[ny][nx] = "."
    return cnt

dis[R-1][0] = "T"  # 시작점을 방문 표시
print(dfs(0, R-1, 1))
