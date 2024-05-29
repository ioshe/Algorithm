# https://www.acmicpc.net/problem/16435

'''
3 10
10 11 13
'''

from sys import stdin
N,l = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

nums.sort()

for i in nums :
    if l >= i :
        l += 1 

print(l)