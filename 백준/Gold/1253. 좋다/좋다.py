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
        hap = nums[left] + nums[right]
        if hap == nums[i] :
            if left == i :
                left += 1
            elif right == i :
                right -= 1
            else:
                count += 1
                left += 1 # 또는 right -= 1, 둘 중 하나를 선택하여 다른 조합 탐색
                break
        elif hap < nums[i] :
            left += 1
        else :
            right -= 1
            #print(nums[i])
        
print(count)