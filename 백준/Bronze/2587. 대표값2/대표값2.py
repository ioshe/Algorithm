# https://www.acmicpc.net/problem/2587

import sys
input = sys.stdin.readlines

nums = list(map(int,input())) 
print(sum(nums) // len(nums))
print(sorted(nums)[2])

