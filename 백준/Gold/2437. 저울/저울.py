# https://www.acmicpc.net/problem/2437

from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
nums.sort()

hap = 1
for i in range(0,n) :
    if hap < nums[i] : 
        break
    hap += nums[i]
print(hap)