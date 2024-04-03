# https://www.acmicpc.net/problem/12738

from sys import stdin

def binary_search(li,target) :
    left,right = 0,len(li)
    while left <= right :
        mid = (left+right) // 2
        if target > li[mid] :
            left = mid + 1
        else :
            right = mid - 1
    # print(left)
    return left
n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

li = []
for i in nums :
    if not li or li[-1] < i :
        li.append(i)
    else :
        li[binary_search(li,i)] = i
    # print(li)

print(len(li))