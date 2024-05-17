import heapq
from sys import stdin

def main():
    index = 0
    T = int(stdin.readline())

    for _ in range(T):
        k = int(stdin.readline())
        min_heap, max_heap = [], []
        entry_finder = {}  # 현재 힙에 있는 원소의 존재 여부를 관리하는 사전
        counter = 0

        for _ in range(k):
            operation, num = stdin.readline().split()
            num = int(num)
            if operation == 'I':
                if num not in entry_finder :
                    entry_finder[num] = 1
                    heapq.heappush(min_heap, num)
                    heapq.heappush(max_heap, -num)
                else : 
                    entry_finder[num] += 1
            elif operation == 'D':
                if num == 1:  # 최댓값 삭제
                    while max_heap and -max_heap[0] not in entry_finder :
                        heapq.heappop(max_heap)
                    if max_heap and -max_heap[0] in entry_finder :
                        if entry_finder[-max_heap[0]] == 1:
                            del(entry_finder[-max_heap[0]])
                            heapq.heappop(max_heap)
                        else :
                            entry_finder[-max_heap[0]] -= 1

                elif num == -1:  # 최솟값 삭제
                    while min_heap and min_heap[0] not in entry_finder :
                        heapq.heappop(min_heap)
                    if min_heap and min_heap[0] in entry_finder :
                        if entry_finder[min_heap[0]] == 1:
                            del(entry_finder[min_heap[0]])
                            heapq.heappop(min_heap)
                        else :
                            entry_finder[min_heap[0]] -= 1

        while min_heap and min_heap[0] not in entry_finder:
            heapq.heappop(min_heap)
        while max_heap and -max_heap[0] not in entry_finder:
            heapq.heappop(max_heap)

        if entry_finder:
            print(f"{-max_heap[0]} {min_heap[0]}")
        else:
            print("EMPTY")

main()
