# https://www.acmicpc.net/problem/2304

'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6
'''

from sys import stdin

n = int(stdin.readline())
# 왼쪽 면의 위치 L, 높이 H
nums = list(map(lambda a : list(map(int,a.split())), stdin.readlines()))
nums.sort(key = lambda a : a[0])
nums = list(enumerate(nums))
# print(nums)

max_position = max(nums, key = lambda x : x[1][1])[0]

left_nums = nums[:max_position+1]

right_nums = nums[max_position:]

# print(left_nums)
# print(right_nums)

size = 0
current_height = 0 
current_position = 0
for index,value in left_nums : 
    if current_height <= value[1] :
        size += ((value[0] - current_position) * current_height)
        current_position = value[0]
        current_height = value[1]
    
    # print(f'{index} 회차 size = {size}, inform ch = {current_height} cp = {current_position} value = {value}')

current_height = right_nums[-1][1][1]
current_position = right_nums[-1][1][0]
for index,value in right_nums[::-1] : 
    if current_height <= value[1] :
        size += ((current_position - value[0]) * current_height)
        current_position = value[0]
        current_height = value[1]
    # print(f'{index} 회차 size = {size}, inform ch = {current_height} cp = {current_position} value = {value}')


print(size + nums[max_position][1][1])

