# https://www.acmicpc.net/problem/13702

'''
4 11
427
541
774
822
'''

from sys import stdin

N,M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readlines()))

start, end = 1, sum(nums) // M

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for num in nums:
        cnt += num // mid

    if cnt >= M:
        start = mid + 1
    else :
        end = mid - 1

print(start - 1)