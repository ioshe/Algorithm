'''
14 40 243
74 39 127 95 63 140 99 96 154 18 137 162 14 88
'''
from sys import stdin

N,S,M = map(int,stdin.readline().split())
nums = [0] + list(map(int,stdin.readline().split()))
dp = {S}
for i in range(1,N+1) :
    temp = dp.copy()
    dp = set()
    for j in temp :
        if 0<= nums[i] + j <= M :
            dp.add(nums[i] + j)
        if 0<= j - nums[i] <= M :
            dp.add(j - nums[i])
    # print(dp)
    if dp == set():
        print(-1)
        exit(0)
print(max(dp))
