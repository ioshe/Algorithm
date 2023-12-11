#https://www.acmicpc.net/problem/1535
MAX_HEALTH = 100
from sys import stdin
text = stdin.read().splitlines()
N = int(text[0])
lost_health = [0]+[*map(int,text[1].split())]
gain_happy = [0]+[*map(int,text[2].split())]
dp =[[0 for i in range(MAX_HEALTH)] for i in range(N+1)]
for i in range(1,N+1) :
    for j in range(1,MAX_HEALTH):
        # if lost_health[i] > j :
        #     dp[i][j]=dp[i-1][j]
        if lost_health[i] <= j :
            dp[i][j] = max(dp[i-1][j-lost_health[i]]+gain_happy[i],dp[i-1][j])
        else :
            dp[i][j]=dp[i-1][j]
        # if lost_health[i]+j < MAX_HEALTH:# and lost_health[i] < MAX_HEALTH:
        #     dp[i][j] = max(dp[i-1][j-lost_health[i]]+gain_happy[i],dp[i-1][j])
        # else :
        #     dp[i][j]=dp[i-1][j]
            # print("이거 동작하니?")
   
# print(dp)
print(dp[-1][-1])