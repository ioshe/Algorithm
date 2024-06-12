# https://www.acmicpc.net/problem/11057

from sys import stdin

n = int(stdin.readline())

old_dp = [1 for i in range(10)]
new_dp = [0 for i in range(10)]

if n == 1 :
    print(10)
    exit(0)

for i in range(n-1) :
    new_dp = [0 for i in range(10)]
    for j in range(0,10) :
        new_dp[j] = sum(old_dp[:j+1]) % 10007
    new_dp[0] = 1
    #print(new_dp)
    old_dp = new_dp.copy()
    
print(sum(new_dp)%10007)