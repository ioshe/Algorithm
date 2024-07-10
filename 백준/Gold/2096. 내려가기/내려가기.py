
from sys import stdin

n = int(stdin.readline())

for i in range(0,n) :
    nums = list(map(int,stdin.readline().split()))
    if i == 0 :
        max_dp = [[0 for j in range(3)] for i in range(2)]
        min_dp = [[float('inf') for j in range(3)] for i in range(2)]

        max_dp[0] = nums[::]
        min_dp[0] = nums[::]
    else :
        reverse = 0 if i%2==1 else 1
        max_dp[i%2][0] = nums[0]+max(max_dp[reverse][0],max_dp[reverse][1])
        max_dp[i%2][1] = nums[1]+max(max_dp[reverse][0],max_dp[reverse][1],max_dp[reverse][2])
        max_dp[i%2][2] = nums[2]+max(max_dp[reverse][1],max_dp[reverse][2])

        min_dp[i%2][0] = nums[0]+min(min_dp[reverse][0],min_dp[reverse][1])
        min_dp[i%2][1] = nums[1]+min(min_dp[reverse][0],min_dp[reverse][1],min_dp[reverse][2])
        min_dp[i%2][2] = nums[2]+min(min_dp[reverse][1],min_dp[reverse][2])
# print(max_dp)
# print(min_dp)
print(max(max_dp[(n-1)%2]),min(min_dp[(n-1)%2]))