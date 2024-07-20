# https://www.acmicpc.net/problem/10819

'''
input : 
6
20 1 15 8 4 10

output : 
62
'''

import sys 
from itertools import permutations 
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
result = 0
for num in permutations(nums) :
    cnt = 0
    hap = 0
    while cnt < n - 1 :
        hap += abs(num[cnt] - num[cnt+1])
        cnt += 1
    if result < hap :
        result = hap

print(result)