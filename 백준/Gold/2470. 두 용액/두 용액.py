# https://www.acmicpc.net/problem/2470
from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

nums.sort()

left = 0
right = n - 1

closet_val = float('inf')

while left < right :
    current = (nums[left] + nums[right])
    # print(f'{nums[left]} +{ nums[right]} =  {current}')
    if abs(current) < abs(closet_val) : 
        closet_val = current
        result = nums[left],nums[right]
        # print(f'result = {result}')
    if current > 0 :
        right -= 1
    elif current < 0 :
        left += 1
    else :
        break

print(result[0],result[1])