# https://www.acmicpc.net/problem/1987


from sys import stdin

r,c = map(int,stdin.readline().split())
map = [stdin.readline().rstrip() for _ in range(r)]

# print(map)
result = 0
def dfs(i,j,visited,map,num,result) :
    for (dx,dy) in [(-1,0),(0,-1),(1,0),(0,1)] :
        nx,ny = i+dx,j+dy
        if 0<=nx<r and 0<=ny<c and not(visited[ord(map[nx][ny]) - 65]) : # 'A' = 65
            visited[ord(map[nx][ny]) - 65] = 1
            result = dfs(nx,ny,visited,map,num+1,result)
            visited[ord(map[nx][ny]) - 65] = 0
        else :
            #print(visited)
            if result < num :
                result = num

    return result
visited = [0 for _ in range(26)]
visited[ord(map[0][0])-65] = 1
result = dfs(0,0,visited,map,1,result)
print(result)
