# https://www.acmicpc.net/problem/13904

from sys import stdin
from heapq import heapify,heappop,heappush,heappushpop
n = int(stdin.readline())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
visited = [False] * 1001
result = 0

nums.sort(key = lambda a : -a[1])
for d,w in nums :
    i = d

    while i > 0 and visited[i] :
        i -= 1

    if i == 0 :
        # 과제를 할 날짜가 없음
        continue
    else :
        visited[i] = True
        result+=w

# p = []
# while queue :
#     while ready_queue and current_day > ready_queue[0][0] - len(ready_queue):
#         # ready_queue[0][0] - len(ready_queue) = ready queue 에 4일차가 2개 쌓여 있으면 최소 3일 부터는 실행해야 하니
#         # 4-2 = 2
#         temp_d,temp_w = heappop(ready_queue)
#         result += temp_w 
#         current_day += 1
#          # ready queue 에 담겨 있는 가장 먼저 처리 할 수 잇는 날짜
#     w,d = heappop(queue)
#     if d >= current_day :
#         heappush(ready_queue,(d,-w))
# result += sum(map(lambda a: a[1],ready_queue))
print(result)