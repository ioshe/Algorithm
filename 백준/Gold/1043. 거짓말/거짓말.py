# https://www.acmicpc.net/problem/1043

import sys 
input = sys.stdin.readline

'''
input : 
4 3 # 사람수 N, 파티수 M
0 # 이야기의 진실을 아는 사람의 수와 번호 그 개수만큼 사람들의 번호가 주어진다.
2 1 2 # 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다. 
1 3 
3 2 3 4

# 과장된 이야기를 할 수 있는 파티 개수의 최댓값
output :
3
'''

def in_party(party,visited) :
    for p in party[1:] :
        if visited[p] :
            return 0
    return 1

def dfs(visited,start,graph) :
    for i in graph[start] :
        if not visited[i] :
            visited[i] = True
            dfs(visited,i,graph)
N,M = map(int,input().split()) # 사람의 수 N, 파티의 수 M
known_true = list(map(int,input().split())) # 이야기의 진실을 아는 사람의 수 와 번호
partys = list(list(map(int,input().split())) for i in range(M))

if known_true == 0 :
    print(M) 
else :
    # dfs로 진실을 알고 있는 사람의 연결 고리를 만들어야 겠네
    graph = {i:set() for i in range(1,N+1)}
    for party in partys :
        for k in range(1,party[0]) :
            graph[party[k]].add(party[k+1])
            graph[party[k+1]].add(party[k])
    #print(graph)
    visited = [False for i in range(N+1)]
    for i in known_true[1:] :
        if not visited[i] :
            visited[i] = True
            dfs(visited,i,graph)
    
    count = 0
    for party in partys :
        count += in_party(party,visited)
    print(count)