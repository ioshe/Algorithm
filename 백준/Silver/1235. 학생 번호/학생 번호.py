#https://www.acmicpc.net/problem/1235

from sys import stdin

nums = stdin.read().splitlines()[1:]
std = len(nums[0])
for size in range(1,std+1) :
    text = []
    for num in nums :
        text.append(num[std-size:])
    if len(text) == len(set(text)) :
        # print(text)
        # print(set(text))
        break

print(size)

