from sys import stdin

def bfs(start,n) :
    count = 0
    queue = [[start,1]]
    visited = [start]
    while queue :
        if len(visited) == n :
            break
        st,ct = queue.pop(0)
        for i in friends[st] :
            if i not in visited :
                visited.append(i)
                count += ct
                # print(f'{start}의 {i}를 방문할 떄 {ct}')
                queue.append([i,ct+1])
    # print(f'{start}의 방문 횟수 {count}')
    return count

n,m = map(int,stdin.readline().split())

friends = {}

for te in stdin.read().splitlines() :
    i, j = map(int,te.split())
    friends.setdefault(i, []).append(j)
    friends.setdefault(j, []).append(i)
# print(friends)
mi = 12502501
id = 0
for i in range(n,0, -1) :
    temp = bfs(i,n)
    # print(f'{mi} / {temp}')
    if mi >= temp :
        id = i
        mi = temp
        # print(f'{i} 로 바뀜')

print(id)