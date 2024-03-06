# https://www.acmicpc.net/problem/1253
from sys import stdin

n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

nums.sort()

count = 0
for i in range(n) :
    left = 0
    right = n - 1

    while left < right :
        if left == i :
            left += 1
            continue
        if right == i :
            right -= 1
            continue

        if nums[left] + nums[right] > nums[i] :
            right -= 1
        elif nums[left] + nums[right] < nums[i] :
            left += 1
        else :
            count += 1
            #print(nums[i])
            break
        
print(count)