# https://www.acmicpc.net/problem/1926

'''
input : 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
output :
4
9
'''
# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
# 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 
# 그림의 넓이란 그림에 포함된 1의 개수이다.

from sys import stdin
from collections import deque

def bfs(i,j,n,m) :
    global nums
    queue = deque([(i,j)])
    size = 1
    while queue :
        x,y = queue.popleft()
        for px,py in [(1,0),(-1,0),(0,1),(0,-1)] :
            nx,ny = px+x,py+y
            if 0<=nx<n and 0<=ny<m and nums[nx][ny] == 1 :
                nums[nx][ny] = 0
                queue.append([nx,ny])
                size += 1
    return size

n,m = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
max_room = count = 0 
for i in range(n) :
    for j in range(m) :
        if nums[i][j] == 1 :
            count +=1
            nums[i][j] = 0 
            max_room = max(bfs(i,j,n,m),max_room)
print(f'{count}\n{max_room}')