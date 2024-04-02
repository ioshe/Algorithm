# https://www.acmicpc.net/problem/12865

from sys import stdin

n,m = map(int,stdin.readline().split())
nums = list(map(lambda a: list(map(int,a.split())), stdin.read().splitlines()))

dp = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(1,n + 1) :
    for j in range(m + 1) :
        if j >= nums[i-1][0] : # nums 에 넣을 수 있는 무게이면
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-nums[i-1][0]]+nums[i-1][1])
        else :
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])