'''
10
1 4 2 3 1 4 2 3 1 2
'''

from sys import stdin

n = stdin.readline()
nums = set(map(int,stdin.readline().split()))
print(*sorted(list(nums)))
