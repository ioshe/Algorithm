#https://www.acmicpc.net/problem/14501
from sys import stdin
N= int(stdin.readline())
counsels = [[int(x) for x in stdin.readline().split()] for i in range(N)]
dp = [0]*N
for i in range(N) :
    dp[i] = max(dp[i], dp[i-1])
    Ti = counsels[i][0]
    if Ti + i-1 < N :
        dp[Ti + i-1] = max(dp[Ti + i-1],dp[i-1] + counsels[i][1])

print(max(dp))