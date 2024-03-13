# https://www.acmicpc.net/problem/11724
from sys import stdin
from collections import deque

def bfs(start,count) :
    global visited
    #print(f'{visited} start : {start}')
    if visited[start] == 0 :    
        queue = deque([start])
        while queue :
            q = queue.popleft()
            #print(f'in while : {q} 번째 {nums[q]}')
            if visited[q] == 0 :
                visited[q] = 1
                queue.extend([j for j in list(nums[q]) if visited[j] == 0])
                #print(queue)
        return count + 1
    return count

n,m = map(int,stdin.readline().split())
data = map(lambda a : list(map(int,a.split())), stdin.read().splitlines())

nums = {i:[] for i in range(1,n+1)}
for i,j in data :
    nums[i].append(j)
    nums[j].append(i)

visited = {key : 0 for key in list(nums.keys())}
count = 0
for i in visited.keys() :
    count = bfs(i,count)

print(count)


