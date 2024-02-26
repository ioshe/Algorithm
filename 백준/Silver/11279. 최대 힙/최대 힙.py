class Maxheap() :
    def __init__(self) :
        self.queue = []

    def insert(self,n) :
        self.queue.append(n)
        last_index = len(self.queue) - 1
        if last_index != 0 :
            # parent_index = (last_index+1) // 2 - 1
            # self.sort(parent_index)
            self.sort(last_index)
    
    def sort(self,last_index) :
        parent_index = (last_index - 1) // 2 
        if parent_index >= 0 and self.queue[last_index] > self.queue[parent_index] :
            self.switch(last_index,parent_index)
            self.sort(parent_index)
        
    def Maxheapify(self,index) :
        left_index = index *2 + 1
        right_index = index *2 + 2
        max_index = index
        limit = len(self.queue) - 1
        if limit >= left_index and self.queue[left_index] > self.queue[max_index] :
            max_index = left_index
        if limit >= right_index and self.queue[right_index] > self.queue[max_index] :
            max_index = right_index
            
        if index != max_index :
            self.switch(max_index,index)
            self.Maxheapify(max_index)

    def delete(self) :
        last_index = len(self.queue) - 1
        if last_index < 0 :
            return 0
        self.switch(0,last_index)
        max_value = self.queue.pop()
        self.Maxheapify(0)
        return max_value

    def switch(self,last_index,parent_index) :
        self.queue[last_index] , self.queue[parent_index] = self.queue[parent_index], self.queue[last_index]
        


a = Maxheap()
result = []
from sys import stdin
for i in range(int(stdin.readline())) :
    temp = int(stdin.readline())
    if temp == 0 :
        result.append(a.delete())
        continue
    a.insert(temp)
# print("결과")
print("\n".join(map(str,result)))