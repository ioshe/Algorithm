from collections import deque
def bfs(n,target) :
    queue = deque([(n,0)])
    visited = set([n])
    while queue :
        temp,count = queue.popleft()
        if temp == target :
            print(count)
            return
        if 2*temp not in visited and temp <= 100000:
            visited.add(2*temp)
            queue.append((2*temp,count+1))
        if temp+1 not in visited and temp <= 100000 :
            visited.add(temp+1)
            queue.append((temp+1,count+1))
        if temp-1 not in visited and temp -1 >= 0:
            visited.add(temp-1)
            queue.append((temp-1,count+1))

N,K = map(int,input().split())
bfs(N,K)
