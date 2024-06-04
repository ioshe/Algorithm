# https://www.acmicpc.net/problem/2822

from sys import stdin

nums = list(enumerate(map(int,stdin.readlines())))
nums.sort(key = lambda a : a[1])
print(sum(map(lambda a : a[1], nums[-5:])))
print(*sorted([i[0]+1 for  i in nums[-5:]]))