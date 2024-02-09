# https://www.acmicpc.net/problem/10844
N = int(input())
dp = [0]+[1]*9
for i in range(1,N):
    mux = dp[:]
    dp[0] = mux[1]
    for j in range(1,9) :
        dp[j] = mux[j-1] + mux[j+1]
    dp[9] = mux[8]
print(sum(dp)%1000000000)