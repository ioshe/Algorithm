# https://www.acmicpc.net/problem/2156
from sys import stdin
n,*num_list = map(int,stdin.read().splitlines())
if n==1 :
    print(num_list[0])
elif n==2:
    print(num_list[1]+num_list[0])
else:
    dp = [[0] for i in range(n)]
    dp[0],dp[1] = num_list[0],num_list[0]+num_list[1]
    dp[2]= max(dp[1],num_list[0]+num_list[2],num_list[1]+num_list[2])
    for i in range(3,n) :
        dp[i] = max(dp[i-1], num_list[i] + dp[i-2], num_list[i] + num_list[i-1] + dp[i-3])
    print(max(dp[n-2:]))