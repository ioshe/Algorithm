import heapq
import sys

input = sys.stdin.read
data = input().splitlines()
N = int(data[0])
classes = []

for i in range(1, N+1):
    start, end = map(int, data[i].split())
    classes.append((start, end))

# 시작 시간 기준으로 수업을 정렬
classes.sort()

# 강의실을 관리할 최소 힙
min_heap = []

for start, end in classes:
    if min_heap and min_heap[0] <= start:
        # 가장 빨리 끝나는 강의실이 현재 강의의 시작시간 이후에 끝나면, 강의실 재사용
        heapq.heappop(min_heap)
    # 새 강의를 현재 강의실에 추가하거나 새 강의실을 사용
    heapq.heappush(min_heap, end)

# 힙의 크기가 필요한 강의실의 최소 수
print(len(min_heap))
