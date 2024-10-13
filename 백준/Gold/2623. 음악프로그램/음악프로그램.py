# https://www.acmicpc.net/problem/2623

'''
input : 
6 3
3 1 4 3
4 6 2 5 4
2 2 3

output : 
6
2
1
5
4
3
'''


from sys import stdin
from collections import defaultdict
N,M = map(int,stdin.readline().split())
order = list(map(lambda a : list(map(int,a.split())), stdin.readlines()))

indegree = [0] * (N + 1)
asdf = defaultdict(list)

# 진입차수 계산
for i in range(M) : 
    for j in range(1,order[i][0]) :
        asdf[order[i][j]].append(order[i][j + 1])
        indegree[order[i][j+1]] += 1

# 진입차수가 0인 거 먼저 진행
queue = []
for i in range(1, N + 1) :
    if indegree[i] == 0 :
        queue.append(i)

#
result = []
while queue :
    now = queue.pop()
    result.append(now)

    for next in asdf[now] :
        indegree[next] -= 1
        if indegree[next] == 0 :
            queue.append(next)

if len(result) != N :
    print(0)
else :
    print("\n".join(map(str,result)))