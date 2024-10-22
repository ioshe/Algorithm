from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(i,j) :
    if dp[i][j] : return dp[i][j]
    dp[i][j] = 1
    for h in range(4) :
        nx, ny = i + dx[h], j + dy[h]
        if 0 <= nx < N and 0 <= ny < N and nums[i][j] < nums[nx][ny] :
            dp[i][j] = max( dp[i][j], dfs(nx,ny) + 1 )
    return dp[i][j]


N = int(stdin.readline())
nums = list(map(lambda a : list(map(int, a.split())),stdin.readlines()))
dp = [[0 for m in range(N)] for k in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0
for i in range(N) :
    for j in range(N) :
        result = max(result, dfs(i,j))

print(result)