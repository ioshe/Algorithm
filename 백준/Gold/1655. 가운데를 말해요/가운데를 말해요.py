from sys import stdin
import heapq

'''
input :
7
1
5
2
10
-99
7
5

output:
1
1
2
2
2
2
5
'''
import heapq
import sys
input = sys.stdin.read

def find_medians(numbers):
    # 최대 힙(왼쪽 그룹), 최소 힙(오른쪽 그룹)
    max_heap = []  # Python의 heapq는 최소 힙만 지원하므로, 최대 힙을 위해 부호를 반대로 함
    min_heap = []
    results = []

    for number in numbers:
        if len(max_heap) == 0 or number <= -max_heap[0]:
            heapq.heappush(max_heap, -number)
        else:
            heapq.heappush(min_heap, number)

        # 최대 힙과 최소 힙의 크기 조정
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 중간값 출력 (항상 최대 힙의 루트)
        results.append(-max_heap[0])

    return results

# 입력을 읽어 처리
data = input().split()
n = int(data[0])  # 숫자의 개수
numbers = list(map(int, data[1:n+1]))

medians = find_medians(numbers)
print("\n".join(map(str,medians)))
