# https://www.acmicpc.net/problem/3273

from sys import stdin

n = int(stdin.readline())
nums = []
nums_dict = {}
for i in list(map(int,stdin.readline().split())) :
    if i not in nums_dict :
        nums_dict[i] = 1
        nums.append(i)
        continue
    nums_dict[i] += 1
nums.sort()
x = int(stdin.readline())

left = 0
right = n-1 
count = 0

while left < right :
    if (temp:=nums[left] + nums[right]) == x :
        count += min(nums_dict[nums[left]],nums_dict[nums[right]])
        left += 1
        right -= 1
    elif temp < x :
        left += 1
    else :
        right -= 1

print(count)

