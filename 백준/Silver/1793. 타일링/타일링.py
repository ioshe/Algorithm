#https://www.acmicpc.net/problem/1793
from sys import stdin
nums = [*map(int,stdin.read().splitlines())]
dp = [1,1,3]
for i in range(3,250+1):
    dp.append(dp[i-1]+dp[i-2]*2)
result = []
result.extend(dp[i] for i in nums)
print("\n".join(map(str,result)))