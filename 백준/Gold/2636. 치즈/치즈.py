# https://www.acmicpc.net/problem/2636

'''
input :
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
output :
3
5
'''

# 입력 :
# 

# 조건 :
# 판의 가장자리에는 치즈가 놓여 있지 않다.
# 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어짐

# 출력 : 
# 치즈가 모두 녹아서 없어지는데 걸리는 시간 
# 모두 녹기 한 시간 전에 남아 있는 치즈조각이 놓여 있는 칸의 개수

from sys import stdin
import sys

sys.setrecursionlimit(10**7)

# 전역변수로 moving_x, moving_y 정의
moving_x = [0, 0, 1, -1]
moving_y = [1, -1, 0, 0]

def dfs(N, M, visited, graph, x, y):
    global moving_x, moving_y  # 함수 내부에서 전역변수 사용을 명시
    visited[x][y] = True  # 현재 위치를 방문 처리
    for i in range(4):
        nx = x + moving_x[i]
        ny = y + moving_y[i]
        # 배열 범위를 벗어나지 않고, 방문하지 않은 공기 중 위치에 대해서 dfs 탐색

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] :
            if graph[nx][ny] == 1 :
                graph[nx][ny] *= -1
            if graph[nx][ny] == 0 :
                dfs(N, M, visited, graph, nx, ny)

def find_melting_cheese(N,M,graph) :
    count = 0
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == -1 :
                graph[i][j] = 0
                count += 1
    return count
    
def solve():
    N, M = map(int, stdin.readline().split())
    graph = [list(map(int, stdin.readline().split())) for _ in range(N)]
    post = 0
    per_count = 0
    while True :
        visited = [[False] * M for _ in range(N)]
        dfs(N, M, visited, graph, 0, 0)  # (0, 0) 위치에서 dfs 시작
        temp = find_melting_cheese(N,M,graph)
        if temp :
            per_count += 1
            post = temp
        else :
            break
    print(per_count)
    print(post)
solve()
