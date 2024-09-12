# https://www.acmicpc.net/problem/1516

'''
input : 
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

output :
10
20
14
18
17
'''

from sys import stdin
from collections import deque
n = int(stdin.readline())
orders = list(map(lambda a : list(map(int, a.split())),stdin.readlines()))
# 각 들어가는데 필요한 거
build_time  = [0] * (n + 1) # 각 건물을 짓는데 필요한 시간
indegree  = [0] * (n + 1) # 각 건물의 진입 차수
graph = [[] for _ in range(n + 1)]  # 건물 간의 의존성 그래프
dp = [0] * (n + 1)  # 각 건물을 완성하는 데 필요한 최소 시간을 저장할 배열
    
# 데이터 넣기
for i in range(1,n+1) :
    build_time[i] = orders[i-1][0]
    for pre  in orders[i-1][1:-1] :
        graph[pre].append(i)
        indegree [i] += 1 

# 위상 정렬을 위한 큐 초기화
queue = deque([])
for i in range(1,n+1) :
    if indegree [i] == 0 :
        queue.append(i)
        dp[i] = build_time[i]  # 선행 건물이 없는 경우, 최소 시간은 건설 시간 자체

# print(f"indegree  {indegree }")
# print(f"queue {queue}")
# 위상 정렬
while queue :
    # 데이터를 뺏는데 앞에서 뺼꺼냐 ㅇ뒤에서 뺄꺼냐 일단 뒤에서 빼보자
    current = queue.popleft()
    for next in graph[current] :
        indegree [next] -= 1
        # 선행 건물이 완성되는 최대 시간에서 현 재 건물의 건설 시간을 더함
        dp[next] = max(dp[next], dp[current] + build_time[next])
        # 모든 선행 건물이 완성된 경우, 큐에 추가
        if indegree[next] == 0:
            queue.append(next)

# 만약 진
print("\n".join(map(str,dp[1:])))
