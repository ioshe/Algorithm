# https://www.acmicpc.net/problem/5557

import sys 
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

MAX_SIZE = 21
dp = [0 for i in range(MAX_SIZE)]

dp[nums[0]] = 1
for i in nums[1:-1] :
    temp = [0 for i in range(MAX_SIZE)] 
    for j in range(MAX_SIZE) :
        if j - i >= 0 :
            temp[j - i] += dp[j]
        if j + i <= 20 :
            temp[j + i] += dp[j]
    for j in range(MAX_SIZE) :
        dp[j] = temp[j]
print(dp[nums[-1]])