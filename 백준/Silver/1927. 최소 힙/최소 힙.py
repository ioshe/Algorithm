# https://www.acmicpc.net/problem/1927
from sys import stdin
class MinHeap(object):
    def __init__(self):
        self.queue = []

    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1

        while 0 <= last_index:
            parent_index = (last_index - 1) // 2
            if 0 <= parent_index and self.queue[parent_index] > self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return 0
        self.swap(0, last_index)
        min_value = self.queue.pop()
        self.minHeapify(0)
        return min_value
    
    def minHeapify(self, i):
        left_index = i * 2 + 1
        right_index = i * 2 + 2
        min_index = i

        if left_index <= len(self.queue) - 1 and self.queue[min_index] > self.queue[left_index]:
            min_index = left_index
        if right_index <= len(self.queue) - 1 and self.queue[min_index] > self.queue[right_index]:
            min_index = right_index
        
        if min_index != i:
            self.swap(i, min_index)
            self.minHeapify(min_index)

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

# stdin 대신 직접 입력 값을 사용하여 테스트
if __name__ == "__main__":
    n = int(stdin.readline())
    nums = list(map(int,stdin.read().splitlines()))
    result = []
    mh = MinHeap()
    
    for i in nums:
        if i == 0:
            result.append(mh.delete())
        else:
            mh.insert(i)

    print("\n".join(map(str, result)))
