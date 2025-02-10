# https://www.acmicpc.net/problem/9237

from sys import stdin
input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

result = 0
for i in range(len(nums)):
    result = max(result, i + nums[i] + 1)

print(result + 1)