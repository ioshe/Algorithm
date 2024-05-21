from sys import stdin
from collections import deque 
import heapq
N,M = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
# 위상 정렬을 관리하기 위한 리스트
# 문제번호가 1~N 까지 이므로 N+1 까지 생성한다.
directed = [0 for i in range(N+1)] 

graph = [[] for i in range(N+1)]
for (a,b) in nums :
    # a번 문제는 b 번 문제보다 먼저 풀어야 한다.
    # 방향성을 기록하기 위한 graph a -> b 
    graph[a].append(b)
    # b의 진입 차수가 생긴다.
    directed[b] += 1

# 진입 차수가 0 인것 부터 push
queue = []
for i in range(1,N+1) :
    if directed[i] == 0 :
        heapq.heappush(queue,i)

'''
A 번 문제는 B 번 문제보다 먼저 푸는 것이 좋다.
input : 4 2
4번 문제는 2번 보다 먼저 풀어야 한다.
2번은 진입 차수가 하나 있는거고
진입 차수 0인 것부터 푸는데 그 순서는 가장 낮은거 
그래서 3이 나오고 3은 1 다음에 풀어야 한다
3을 result.append()
1의 진입차수가 0이 된다면(다른 것들이 1을 먼저 풀어야 한다는 조건이 없으면)
queue 에 넣는다.
'''
result = []
while queue :
    temp = heapq.heappop(queue)
    result.append(temp)
    for i in graph[temp] :
        directed[i] -= 1
        if directed[i] == 0 :
            heapq.heappush(queue,i)
print(" ".join(map(str,result)))