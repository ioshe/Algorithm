# https://www.acmicpc.net/problem/23059



# 먼저 구매해야 하는 아이템은끼리는 사전 순으로 구매한다.


# 위상 정렬이랑, 뭔가 여러개의 사전순을 비교하지 않게 하기 위해서 인덱싱을 해볼까

from sys import stdin
from collections import defaultdict
import heapq

n = int(stdin.readline())
order_items = list(map(lambda a : a.strip().split(),stdin.readlines()))
graph = defaultdict(list) # 
indegree = defaultdict(int)
index_set = set()

for a,b in order_items :
    # 아이템 A는 아이템 B를 구입하기 위해 앞서 구매해야 하는 것
    graph[a].append(b)
    index_set.add(a)
    index_set.add(b)
    indegree[b] += 1

# 위상 정렬을 위한 queue 생성
queue = []
for i in index_set : 
    if indegree[i] == 0 :
        heapq.heappush(queue,(0,i)) 
# print(queue)
# print(graph)
# print(index_item)     
# print(indegree)
# 위상 정렬
result = []

while queue :
    depth,current = heapq.heappop(queue)
    result.append(current)
    if current in graph :
        for next in sorted(graph[current]) :
            indegree[next] -=1 
            if indegree[next] == 0 :
                heapq.heappush(queue,(depth+1,next))

if len(result) != len(index_set) :
    print(-1)
else:
    print("\n".join(result))