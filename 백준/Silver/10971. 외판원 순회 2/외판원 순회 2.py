# https://www.acmicpc.net/problem/10971

from sys import stdin

def dfs(n, nums, visited, cost, count, current, lowest):
    if count == n - 1:
        if nums[current][0] != 0:  # 마지막 도시에서 출발 도시로 돌아오는 비용이 0이 아닌 경우
            lowest[0] = min(lowest[0], cost + nums[current][0])
        return
    
    if lowest[0] <= cost:
        return
    
    for next in range(n):
        if not visited[next] and nums[current][next] != 0:
            visited[next] = True
            dfs(n, nums, visited, cost + nums[current][next], count + 1, next, lowest)
            visited[next] = False

def solution() :
    n = int(stdin.readline())
    nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
    lowest = [float('inf')]
    visited = [False] * n
    visited[0] = True  # 시작 도시는 방문한 것으로 설정
    dfs(n,nums,visited,0,0,0,lowest)
    print(lowest[0])

solution()