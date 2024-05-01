from sys import stdin
'''
input : 
8
1 6 2 5 7 3 5 6
output : 
5
'''

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [1 for i in range(n)]
for i in range(1,n) :
    for j in range(0,i) :
        if nums[j] < nums[i] :
            dp[i] = max(dp[j]+1,dp[i])

print(max(dp))