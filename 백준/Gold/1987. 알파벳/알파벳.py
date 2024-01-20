# https://www.acmicpc.net/problem/1987


from sys import stdin

r,c = map(int,stdin.readline().split())
map = [stdin.readline().rstrip() for _ in range(r)]

# print(map)
result = set()
def dfs(i,j,visited,map,num) :
    # for i in range(r) :
    #     for j in range(c) :
    #         print(map[i][j])
    # if map[i][j] in visited :
    #     result.add(len(visited))
    #     print(visited)
    #     return

    # visited.append(map[i][j])

    for (dx,dy) in [(-1,0),(0,-1),(1,0),(0,1)] :
        nx,ny = i+dx,j+dy
        if 0<=nx<r and 0<=ny<c and not(visited[ord(map[nx][ny]) - 65]) : # 'A' = 65
            visited[ord(map[nx][ny]) - 65] = 1
            dfs(nx,ny,visited,map,num+1)
            visited[ord(map[nx][ny]) - 65] = 0
        else :
            #print(visited)
            result.add(num)

visited = [0 for _ in range(26)]
visited[ord(map[0][0])-65] = 1
dfs(0,0,visited,map,1)
print(max(result))

