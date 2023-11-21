#https://www.acmicpc.net/problem/10422
from sys import stdin
dp = [0] * 5002
dp[0] = 1 
dp[2] = 1
dp[4] = 2
#dp[4] = 2
for i in range(6,5002,2) :
    for j in range(0,i,2) :
        dp[i]+= (dp[i-j-2] * dp[j])
        dp[i] %= 1000000007

result = []
note = list(map(int,stdin.read().splitlines()))
for i in note[1:] :
    result.append(dp[i])    
print("\n".join(map(str,result)))