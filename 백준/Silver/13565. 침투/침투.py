# https://www.acmicpc.net/problem/13565

'''
input : 
5 6
010101
010000
011101
100011
001011

output :
NO
'''
from sys import stdin
from collections import deque

def bfs(i,m,n) :
    global nums
    queue = deque([(0,i)])
    while queue :
        x,y = queue.popleft()
        for px,py in [(0,1),(1,0),(0,-1),(-1,0)] :
            nx,ny = x+px,y+py 
            if 0<=nx<m and 0<=ny<n and nums[nx][ny] == 0 :
                if nx == m - 1 :
                    print("YES")
                    exit(0)
                    
                nums[nx][ny] = 1
                queue.append((nx,ny))

m,n = map(int,stdin.readline().split()) # m은 행 n은 열
nums = list(map(lambda a : list(map(int," ".join(a).split())),stdin.readlines()))
contact = False
for i in range(n) :
    if nums[0][i] == 0 :
        nums[0][i] = 1
        bfs(i,m,n)
print("NO")
        
