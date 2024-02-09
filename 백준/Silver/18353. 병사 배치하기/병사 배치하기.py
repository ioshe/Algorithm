#https://www.acmicpc.net/problem/18353
from sys import stdin

def binary_search(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == target :
            return mid
        if arr[mid] < target :
            end = mid-1
        else :
            start = mid+1
    return start

n = int(stdin.readline())
nums = [*map(int,stdin.readline().split())]
sorting_nums = []

for i in nums :
    #print(sorting_nums)
    if not(sorting_nums) or sorting_nums[-1]>i :
        sorting_nums.append(i)
        continue
    sorting_nums[binary_search(sorting_nums,i)] = i
print(len(nums) - len(sorting_nums))