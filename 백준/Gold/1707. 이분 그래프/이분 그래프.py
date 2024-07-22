# https://www.acmicpc.net/problem/1707

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장

    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:  # 아직 방문하지 않은 노드
            # -group : 현재 노드의 그룹과 다른 값 전달
            result = DFS(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:  # 이미 방문한 곳 중에서 노드가 현재 그룹과 같으면 이분 그래프가 아님
                return False
    return True

# 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서
# 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
K = int(input())
for i in range(K) :
    V,E = map(int,input().split())    
    visited = [0 for i in range(V+1)]
    graph = {i:[] for i in range(1,V+1)}
    for j in range(E) :
        v,e = map(int,input().split())
        graph[e].append(v)
        graph[v].append(e)

    for i in range(1, V+1):
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result:
                break
    print("YES") if result else print("NO")


