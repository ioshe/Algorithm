from sys import stdin
from collections import defaultdict
import heapq

# 관계 수 입력
n = int(stdin.readline())

# 그래프 및 진입 차수, 아이템 집합 초기화
graph = defaultdict(list)
indegree = defaultdict(int)
item_set = set()

# 관계 입력 및 그래프 구성
for _ in range(n):
    a, b = stdin.readline().strip().split()
    graph[a].append(b)
    item_set.add(a)
    item_set.add(b)
    indegree[b] += 1
    # 진입 차수가 없는 아이템도 indegree 딕셔너리에 포함
    if a not in indegree:
        indegree[a] = indegree.get(a, 0)

# 초기 구매 가능한 아이템 찾기
heap = []
for item in item_set:
    if indegree[item] == 0:
        heapq.heappush(heap, item)

result = []

# 위상 정렬 시작
while heap:
    current_purchasable_items = []

    # 현재 구매 가능한 모든 아이템을 힙에서 추출
    while heap:
        current_purchasable_items.append(heapq.heappop(heap))

    # 추출한 아이템들을 처리
    for item in current_purchasable_items:
        result.append(item)
        for neighbor in graph[item]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

# 모든 아이템을 구매했는지 확인
if len(result) != len(item_set):
    print(-1)
else:
    for item in result:
        print(item)
