# https://www.acmicpc.net/problem/17144

from sys import stdin


'''
input : 
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
'''
def find_airmachine(R,C,nums) :
    for i in range(R) :
        for j in range(C) :
            if nums[i][j] == -1 : # -1 이 공기청정기 위치
                return [i,i+1] # 공기 청저기는 항상 1열에 두칸으로 존재하니 처음 만난거에서 행만 +1 해서 넘겨준다.
            
def dust_spread(R,C,i,j,visited) :
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    how_many = nums[i][j] // 5 # 환상되는 양 (소수점은 버린다.)
    count = 0
    for n in range(4) :
        nx,ny = i+dx[n],j+dy[n] # 인전한 네 방향으로 확산
        if 0 <= nx < R and 0 <= ny < C and nums[nx][ny] != -1: # 판안에 있으면서 공기청정기가 아닌 곳에 확산
            visited[nx][ny] += how_many
            count += 1
    visited[i][j] += nums[i][j] - (count * how_many) # 확산된 방향의 개수만큼

def dust_checked(R,C,nums,visited) :
    for i in range(R) :
        for j in range(C) :
            if nums[i][j] != 0 and nums[i][j] != -1 :
                dust_spread(R,C,i,j,visited)

def push_air_row(row,start,end,direction,visited) :
    temp = visited[row][start]
    for j in range(start,end,direction) :
        temp_next = visited[row][j+direction]
        visited[row][j+direction] = temp
        temp = temp_next

def push_air_col(col,start,end,direction,visited) :
    temp = visited[start][col]
    for k in range(start,end,direction) :
        temp_next = visited[k+direction][col]
        visited[k+direction][col] = temp
        temp = temp_next


def push_airmachine(R,C,visited,air_location) :
    i = air_location[0]
    k = air_location[1]
    push_air_col(0,0,i-1,1,visited) # 내리기
    push_air_col(0,R-1,k-1,-1,visited) # 올리기

    #print("\n".join(" ".join(map(str,a)) for a in visited))
    #print()
    # <-
    # 당겨오기
    push_air_row(0,C-1,0,-1,visited)
    push_air_row(-1,C-1,0,-1,visited)
    #print("\n".join(" ".join(map(str,a)) for a in visited))
    #print()
    # ㅅ
    # | 위로 올리기 
    push_air_col(-1,i,-1,-1,visited)
    push_air_col(-1,k,R-1,1,visited) # 내리기
    #print("\n".join(" ".join(map(str,a)) for a in visited))
    #print()
    # ->
    # 오른쪽으로 밀기
    push_air_row(i,1,C-1,1,visited)
    push_air_row(k,1,C-1,1,visited)
    visited[i][1] = visited[k][1] = 0 #공기청정기에서 나온 공기는 0
    #print("\n".join(" ".join(map(str,a)) for a in visited))
    #print()


R,C,T = map(int,stdin.readline().split())
nums = list(map(lambda a : list(map(int,a.split())),stdin.readlines()))
count = 0
air_location = find_airmachine(R,C,nums)

while count < T :
    count += 1 
    visited = [[0 for j in range(C)] for i in range(R)]
    
    dust_checked(R,C,nums,visited)
    push_airmachine(R,C,visited,air_location)
    visited[air_location[0]][0] = visited[air_location[1]][0] = -1
    nums = visited.copy()

print(sum(sum(i) for i in visited) + 2)