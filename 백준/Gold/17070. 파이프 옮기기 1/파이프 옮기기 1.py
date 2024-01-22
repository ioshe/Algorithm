# https://www.acmicpc.net/problem/17070

# 새 집의 크기는 N×N의 격자판
# 각각의 칸은 (r, c)로 나타낼 수 있다. 여기서 r은 행의 번호, c는 열의 번호이고, 
# 행과 열의 번호는 1부터 시작
# 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.
# 가로 이동 시 1 1 세론는 1/1 대각선은 11/11
# 가로는 오른쪽과, 대각선으로 이동가능
# 세로는 세로와, 대각선으로 이동가능
# 대각선은 가로, 세로, 대각선 가능

# 가장 처음에 파이프는 (1, 1)와 (1, 2)를 차지하고 있고, 방향은 가로이다. 
# 파이프의 한쪽 끝을 (N, N)로 이동시키는 방법의 개수



# 입력
#  N(3 ≤ N ≤ 16)
# N개의 줄에는 집의 상태, 빈 칸은 0, 벽은 1

from sys import stdin

n = int(stdin.readline())
maps = [list(map(int,stdin.readline().split())) for i in range(n)]
rotation = [0,1,2] # 0: horizental 1: vertical 3: diagonal
path = 0
def dfs(i,j,rotation) :
    global path,maps
    if not(0<=i<n) or not(0<=j<n) or maps[i][j] == 1 :
        return 
    if rotation == 2 and (maps[i-1][j] == 1 or maps[i][j-1] == 1):
        return
    if i == n-1 and j == n-1 :
        path +=1
        return
    
    if rotation == 0 : # 파이프가 가로 방향이라면 x와 대각선만 가능
        dfs(i,j+1,0) #가로방향으로 한칸 이동
        dfs(i+1,j+1,2)
    
    if rotation == 1 : # 파이프가 세로 방향이라면 y와 대각선만 가능
        dfs(i+1,j,1)
        dfs(i+1,j+1,2)
    
    if rotation == 2 :
        dfs(i,j+1,0)
        dfs(i+1,j,1)
        dfs(i+1,j+1,2)

if n != 16 :
    if (maps[0][2]==1 or (maps[n-1][n-2] ==1 and maps[n-2][n-1]==1)) :
        print(0)
    else :
        dfs(0,1,0)
        print(path)
else : 
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    dp[0][1][0] = 1  # 초기 조건 설정

    for r in range(n):
        for c in range(n):
            # 가로 이동
            if c + 1 < n and maps[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][0] + dp[r][c][2]
            
            # 세로 이동
            if r + 1 < n and maps[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][1] + dp[r][c][2]

            # 대각선 이동
            if r + 1 < n and c + 1 < n and maps[r + 1][c] == 0 and maps[r][c + 1] == 0 and maps[r + 1][c + 1] == 0:
                dp[r + 1][c + 1][2] += dp[r][c][0] + dp[r][c][1] + dp[r][c][2]

    print(sum(dp[n - 1][n - 1]))