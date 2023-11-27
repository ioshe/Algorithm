#https://www.acmicpc.net/problem/9465
from sys import stdin
result = []
for i in range(int(stdin.readline())) :
    n = int(stdin.readline())
    nums = [[*map(int,stdin.readline().split())] for i in range(2)]
    dp = [[0 for i in range(n)] for i in range(2)]
    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    # print("\n".join(map(str,dp)))
    if n == 2 :
        dp[0][1] = dp[0][0] + nums[1][1]
        dp[1][1] = dp[1][0] + nums[0][1]
    else :
        for j in range(1,n) :
            for i in range(2) :
                #dp[i][j] = max(nums[i][j]+nums[(i+1)%2][j-1]+dp[i][j-2],nums[i][j]+dp[(i+1)%2][j-2])
                dp[i][j] = max(nums[i][j]+dp[(i+1)%2][j-1],nums[i][j]+dp[(i+1)%2][j-2])
    result.append(max(dp[0][-1],dp[1][-1]))
print("\n".join(map(str,result)))