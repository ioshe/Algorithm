# https://www.acmicpc.net/problem/17298


'''
input : 
4
3 5 2 7

output :
5 7 7 -1
'''
from sys import stdin
from heapq import heappush, heappop
n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))

queue = []
result = [-1 for i in range(n)]
for index, value in enumerate(nums) :
    if index > 0 and value > min_value :
        while queue and queue[0][0] < value :
            qu_value, qu_index = heappop(queue)
            result[qu_index] = value
        min_value = value
    else :
        min_value = value
    heappush(queue,(value,index))
print(" ".join(map(str,result)))