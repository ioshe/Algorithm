#https://www.acmicpc.net/problem/11053
import sys

def binary_search(lis, target) :
    left = 0
    right = len(lis)-1
    while left <= right :
        mid = (left+right)//2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    #print(f'{target} 값은 {left}를 리턴함')
    return left

a = int(sys.stdin.readline())
num_list = [*map(int,sys.stdin.readline().split())]
result = []
for i in range(len(num_list)) :
    if not result or result[-1] < num_list[i] :
        result.append(num_list[i])
    # elif result[-1] == num_list[i] :
    #     continue
    else :
        index = binary_search(result,num_list[i])
        result[index] = num_list[i]

print(len(result))