from sys import stdin
from collections import defaultdict, deque

N = int(stdin.readline())
M = int(stdin.readline())
data = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
graph = defaultdict(set)

for i in range(M) :
    graph[data[i][0]].add(data[i][1])
    graph[data[i][1]].add(data[i][0])

queue = deque([(1,0)])
visited = [0] * (N + 1)

while queue :
    current,indgreee = queue.popleft()
    if indgreee <=2 and not visited[current] :
        visited[current] = 1
        for next in graph[current] :
            if not visited[next] :
                queue.append((next,indgreee+1))

print(sum(visited)-1)
# print(visited)