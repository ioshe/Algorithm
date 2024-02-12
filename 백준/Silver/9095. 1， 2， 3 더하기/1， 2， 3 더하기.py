import sys
input = sys.stdin.readline
dp=[0]*11
dp[1] = 1
dp[2] = 2
dp[3] =4

for i in range(4,11) :
    sum = 0
    for j in range(i-3,i):
        sum+=dp[j]
    dp[i] = sum
for _ in range(int(input().rstrip())) :
    print(dp[int(input().rstrip())])