# https://www.acmicpc.net/problem/1715
import sys, heapq
n,*num_list = map(int,sys.stdin.readlines())
sum_num = 0
heapq.heapify(num_list)
while n>1 :
    first = heapq.heappop(num_list)
    second = heapq.heappop(num_list)
    sum_num+=first+second
    #print(f'{sum_num}+={first}+{second}')
    heapq.heappush(num_list,first+second)
    n-=1
print(sum_num)