# https://www.acmicpc.net/problem/1817

from sys import stdin

N,M = map(int,stdin.readline().split())
if N == 0:
    print(0)
    exit(0)
nums = list(map(int,stdin.readline().split()))

box = 0
count = 1
for i in range(N):
    if box + nums[i] > M:
        box = nums[i]
        count += 1
    else:
        box += nums[i]

print(count)