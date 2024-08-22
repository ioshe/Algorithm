# https://www.acmicpc.net/problem/2638

from sys import stdin
import sys 
import sys
sys.setrecursionlimit(10**6)
'''
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

def dfs(N,M,nums,i,j,visited) :
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for n in range(4) :
        nx,ny = dx[n]+i, dy[n]+j
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if nums[nx][ny] == 0 :
                visited[nx][ny] = True # 바깥 쪽을 뜻하는 -1 
                dfs(N,M,nums,nx,ny,visited)
            elif nums[nx][ny] >= 1 :
                nums[nx][ny] += 1 # 공기랑 닿으면 
        
N, M = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
count = 0
while True :
    count += 1
    re = False
    visited = [[False for j in range(M)] for i in range(N)]
    # 모눈 종이의 맨 가장자리에는 치즈가 놓이지 않으므로 0,0 은 무조건 외부공기다
    dfs(N,M,nums,0,0,visited)

    # dfs 의 결과로 외부공기와 닿은 치즈는 +1 이 될 것이다.
    # print("\n".join(str(i) for i in nums))
    for i in range(N) :
        for j in range(M) :
            if nums[i][j] >= 3 :
                nums[i][j] = 0
            if nums[i][j] >= 1 : # 다음 처리할 때 중복 처리를 방지하기 위해
                nums[i][j] = 1
                re = True
    if not(re) :
        break
print(count)



