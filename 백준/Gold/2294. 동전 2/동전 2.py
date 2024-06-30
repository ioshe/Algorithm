# https://www.acmicpc.net/problem/2294

from sys import stdin

N,K = map(int,stdin.readline().split())
nums = list(map(int,stdin.readlines()))
pro_nums = []

for i in nums :
    if i <= K :
        pro_nums.append(i)
pro_nums.sort()
dp = [10001 for i in range(K+1)]
for i in pro_nums :
    dp[i] = 1

for i in range(pro_nums[0],K) : 
    if dp[i] :
        for j in pro_nums :
            if i + j <= K :
                dp[i + j] = min(dp[i] + 1,dp[i+j])

# print(dp)
if dp[-1] == 10001 :
    print(-1)
else :
    print(dp[-1])