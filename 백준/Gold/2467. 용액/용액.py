# https://www.acmicpc.net/problem/2467

'''
5
-99 -2 -1 4 98
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

left = 0
right = n - 1
result = (0, 0)
min_abs_sum = float('inf')

while left < right:
    current_sum = nums[left] + nums[right]
    
    if abs(current_sum) < min_abs_sum:
        min_abs_sum = abs(current_sum)
        result = (nums[left], nums[right])
    
    if current_sum == 0:
        break
    elif current_sum > 0:
        right -= 1
    else:
        left += 1

# 오름차순 출력
print(*sorted(result))
