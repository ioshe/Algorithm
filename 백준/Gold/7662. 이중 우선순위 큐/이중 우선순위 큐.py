# https://www.acmicpc.net/problem/7662
'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''

import heapq
from sys import stdin

def isEmpty(nums) :
	# nums에 1인 데이터가 하나라도 있으면 비어있지 않은 것
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(stdin.readline())

for _ in range(T) :
    N = int(stdin.readline())
    # 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n
    min_heap = []
    max_heap = []
    entry_finder = {}
    counter = 0
    
    for _n in range(N) :
        co = stdin.readline().split()
        op, value = co[0], int(co[1])
        if op == "I" :
            if value in entry_finder :
                entry_finder[value] += 1
                continue
            heapq.heappush(min_heap,value)
            heapq.heappush(max_heap,-value)
            entry_finder[value] = 1
            continue
        elif op == 'D':
            if not isEmpty(entry_finder.items()) :
                if value == 1:  # Delete max
                    while -max_heap[0] not in entry_finder or entry_finder[-max_heap[0]] < 1 :
                        temp = -heapq.heappop(max_heap)
                        if temp in entry_finder :
                            del(entry_finder[temp])
                    entry_finder[-max_heap[0]] -= 1
                elif value == -1:  # Delete min
                    while min_heap[0] not in entry_finder or entry_finder[min_heap[0]] < 1 :
                        temp = heapq.heappop(min_heap)
                        if temp in entry_finder :
                            del(entry_finder[temp])
                    entry_finder[min_heap[0]] -= 1
        
    if isEmpty(entry_finder.items()) :
        print('EMPTY')
    else :
        while -max_heap[0] not in entry_finder or entry_finder[-max_heap[0]] < 1 :
            heapq.heappop(max_heap)
        while min_heap[0] not in entry_finder or entry_finder[min_heap[0]] < 1 :
            heapq.heappop(min_heap)
        print(f'{-max_heap[0]} {min_heap[0]}')

