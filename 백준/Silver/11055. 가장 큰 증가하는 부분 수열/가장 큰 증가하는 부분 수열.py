from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
dp = [nums[i] for i in range(n)]


for i in range(1,n) :
    for j in range(0,i) : 
        if nums[i] > nums[j] : 
            dp[i] = max(dp[i],dp[j]+nums[i])

print(max(dp))