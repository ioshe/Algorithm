# https://www.acmicpc.net/problem/14503
from sys import stdin
n,m = map(int,stdin.readline().split())
r,c,d = map(int,stdin.readline().split())
maps =  [list(map(int,stdin.readline().split())) for i in range(n)]
rotation = [(-1,0),(0,1),(1,0),(0,-1)]
#0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽

def blank_check(r,c,maps) :
    for x,y in rotation : 
        nx,ny = r+x,c+y 
        if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 0:
            return False
    return True

count = 0

while True :
    if maps[r][c] == 0 : #현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
        
        count +=1 
        #maps[r][c] = count
        maps[r][c] = -1
          
        # print(f'{r},{c}를 {count} 횟수로 닦음')

    if blank_check(r,c,maps) : #현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        x,y = rotation[(d+2)%4]
        nx,ny = x+r,y+c
        if maps[nx][ny] != 1 :    
            r,c = nx,ny #바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        else :
            break #바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.

    else : # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,           
        d = (d-1)%4 #반시계 방향으로 90도 회전한다.
        x,y = rotation[d]
        nx,ny = x+r, y+c
        if maps[nx][ny] == 0:  #바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            r,c = nx,ny
        #1번으로 돌아간다.
# print()
# print("\n".join(" ".join(map(str,ma)) for ma in maps))
print(count)