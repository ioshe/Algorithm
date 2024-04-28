# https://www.acmicpc.net/problem/1940

from sys import stdin

text = stdin.read().splitlines()
n = int(text[0])
m = int(text[1])
nums = list(map(int,text[2].split()))

nums.sort()
left = 0
right = len(nums) - 1

count = 0
while left < right :
    if nums[left] + nums[right] < m :
        left += 1
    elif nums[left] + nums[right] > m :
        right -=1
    else :
        count +=1
        left += 1
        right -= 1

print(count)