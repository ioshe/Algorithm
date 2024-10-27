# https://www.acmicpc.net/problem/1082
from sys import stdin

INF = 5001
N = int(stdin.readline())
P = list(map(int,stdin.readline().split()))
M = int(stdin.readline())

dp = [-INF for _ in range(M+1)]

for i in range(N-1, -1 ,-1) :
    room = P[i] 
    for j in range(room, M + 1) :
        dp[j] = max(dp[j], dp[j-room] * 10 + i , i)
print(dp[M])