from sys import stdin


class abs_heap :
    def __init__(self) :
        self.queue = []

    def insert(self,n) :
        self.queue.append(n)
        last_index = len(self.queue) - 1 
        parent_index = (last_index-1) // 2 
        while parent_index >= 0 and (abs(self.queue[last_index]) < abs(self.queue[parent_index]) or (abs(self.queue[last_index]) == abs(self.queue[parent_index]) and self.queue[last_index] < self.queue[parent_index])):
            self.switch(parent_index, last_index)
            last_index = parent_index
            parent_index = (parent_index - 1) // 2
    
    def delete(self) :
        if len(self.queue) == 0:
            return 0
        out = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.heapify(0)
        return out

    def heapify(self,parent_index) :
        smallest = parent_index
        left_index = 2 * parent_index + 1
        right_index = 2 * parent_index + 2

        if left_index < len(self.queue) and (abs(self.queue[left_index]) < abs(self.queue[smallest]) or (abs(self.queue[left_index]) == abs(self.queue[smallest]) and self.queue[left_index] < self.queue[smallest])):
            smallest = left_index

        if right_index < len(self.queue) and (abs(self.queue[right_index]) < abs(self.queue[smallest]) or (abs(self.queue[right_index]) == abs(self.queue[smallest]) and self.queue[right_index] < self.queue[smallest])):
            smallest = right_index

        if smallest != parent_index:
            self.switch(parent_index, smallest)
            self.heapify(smallest)


    def switch(self,i,j) :
        self.queue[i],self.queue[j] = self.queue[j],self.queue[i]

n = stdin.readline()
nums = map(int,stdin.read().splitlines())
result = []
a = abs_heap()
for i in nums :
    if i == 0 :
        result.append(a.delete())
    else :
        a.insert(i)

print("\n".join(map(str,result)))