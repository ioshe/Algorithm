# https://www.acmicpc.net/problem/13975

'''
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''

from sys import stdin
from heapq import heappush,heappop
T = int(stdin.readline())
result = []
for _ in range(T) :
    n = int(stdin.readline())
    nums = []
    for i in list(map(int,stdin.readline().split())) : heappush(nums,i) 
    hap = 0
    while len(nums) > 1 :
        a = heappop(nums)
        b = heappop(nums)
        hap += a+b
        heappush(nums,a+b)
        # print(nums)
    result.append(hap)
print("\n".join(map(str,result)))
