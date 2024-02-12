#https://www.acmicpc.net/problem/20500
dp = [0,1,1]
n=int(input())
for i in range(3,n) :
    dp.append(((dp[i-1]+dp[i-2]*2))%1000000007)
print(dp[n-1])