# https://www.acmicpc.net/problem/2056

'''
input : 
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

output :
23
'''

# input : 수행해야 할 작업 N개 (3 <= N < 10000) 
# 각 작업마다 (1 <= 시간 < 100) 이 정수로 주어짐
# N+1번쨰 줄은 N번 작업을 가각 나타낸다. 


# condition : 선행관계, K 번 자업에 대해서 선행 작업들의 번호는 1이상 K-1 이하
# 작업들 중에는, 그것에 대해 선행 관계에 있는 작업이 하나도 없느 작업이 반드시 하나 이상 존재한다. -> 1번 자겅ㅂ
# 서로 선행 관계가 없는 작업들은 동시에 수행 가능함.

# output : 모든 작업을 완료하기 위해 필요한 최소 시간

from sys import stdin
from collections import defaultdict

n = int(stdin.readline())
tasks = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
graph = defaultdict(list)
task_costs = [0] * (n+1)
indegree = [0] * (n+1)
dp = [0] * (n+1)
# 해당 작업에 걸리는 시간 / 그 작업에 대해 선행 관계에 있는 작업들의 개수 / 선행 관계에 있는 작업들의 번호
for index,task in enumerate(tasks) :
    task_costs[index+1] = task[0]
    indegree[index+1] = task[1]
    for i in task[2:] :
        graph[i].append(index+1)

# 위상 정렬을 위한 queue 생성
queue = []
for i in range(1,n+1) :
    if indegree[i] == 0 :
        queue.append(i)
        dp[i] = task_costs[i]

result = 0
while queue :
    current = queue.pop()
    result += dp[current]
    for next in graph[current] :
        indegree[next] -= 1 
        dp[next] = max(dp[next], dp[current]+task_costs[next])
        if indegree[next] == 0 :
            queue.append(next)  
            
print(max(dp))
