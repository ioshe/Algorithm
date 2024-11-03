# https://www.acmicpc.net/problem/2012

from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
nums = [0] + list(map(int,stdin.readlines()))
result = 0
nums.sort()
for i in range(1,n+1) :
    result += abs(i - nums[i])

print(result)