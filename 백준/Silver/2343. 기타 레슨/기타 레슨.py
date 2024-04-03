#  https://www.acmicpc.net/problem/2343

from sys import stdin

N,M = map(int,stdin.readline().split())
nums = list(map(int,stdin.readline().split()))

left = max(nums)
right = sum(nums)

while left <= right :
    mid = (left + right) // 2
    count = 1
    temp = 0
    for i in nums :
        if i > mid : 
            left = i
            break
        if temp + i > mid :
            temp = i
            count += 1
        else :
            temp += i
    # print(f'left {left} right {right} mid {mid} count {count} temp {temp}')
    if count > M :
        left = mid + 1
    else :
        right = mid - 1
    
print(left)