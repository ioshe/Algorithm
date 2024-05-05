# https://www.acmicpc.net/problem/2792

'''
input :
5 2
7
4
output :
3
'''

from sys import stdin
N,M = map(int,stdin.readline().split())
nums = list(map(int,stdin.readlines()))

left,right = 1,sum(nums)

while left <= right :
    mid = (left + right) // 2
    count = 0
    for i in nums :
        # if i < mid :
        #     # 한명은 한 종류의 사탕만 받을 수 있다는 조건으로 인해 
        #     # 현재 나눠줄 수 있는 캔디(i)보다 많은 양(mid)을 나눠줘야 한다면 right 를 줄여야 함
        #     right = mid - 1
        #     break
        # i%N 의 나머지가 있다면 + 1명 더 나눠줄 수 있는 거임
        count += i // mid if i % mid == 0 else i // mid + 1
        
    # right left 를 조정하는 기준은 mid로 나눠주엇을 때 몇명에게 나눠 줄 수 있는지
    if count > N : 
        left = mid + 1
    else :
        right = mid - 1
print(left)