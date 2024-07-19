# https://www.acmicpc.net/problem/1520

'''
input : 
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

output :
3
'''

def dfs(M,N,nums,i,j) :
    if i == M-1 and j == N-1 :
        return 1
    if dp[i][j] != -1 :
        return dp[i][j]
    cnt = 0
    for di in range(4) :
        x,y = i+dx[di], j+dy[di]
        if 0 <= x < M and 0 <= y < N and nums[x][y] < nums[i][j]:
            cnt += dfs(M,N,nums,x,y)
    dp[i][j] = cnt
    return dp[i][j]

import sys 
from sys import stdin

sys.setrecursionlimit(10**8)
M,N = map(int,stdin.readline().split())
dp = [[-1] * N for _ in range(M)]
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
dx, dy = [1,-1,0,0], [0,0,1,-1]
print(dfs(M,N,nums,0,0))
