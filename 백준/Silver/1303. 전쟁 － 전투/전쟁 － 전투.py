from sys import stdin

def bfs(i,j,word,graph,count) :
    graph[i][j] = ' '
    global moving,n,m
    for x,y in moving :
        nx,ny = x+i,y+j
        if 0<=nx<m and 0<=ny<n and word == graph[nx][ny] :
            # print()
            # print("\n".join("".join(graph[i]) for i in range(5)))
            # print()
            count = bfs(nx,ny,word,graph,count+1)
    return count

n,m = map(int,stdin.readline().split())
graph = [" ".join(stdin.readline()).split() for _ in range(m)]
moving = [(0,1),(1,0),(-1,0),(0,-1)]
team = {'W':0,'B':0}
for i in range(m) :
    for j in range(n) :
        if graph[i][j] != ' ' :
            team[graph[i][j]] += bfs(i,j,graph[i][j],graph,1) ** 2
            #print(team)
            #team[graph[i][j]] += bfs(i,j,graph[i][j],graph,1) ** 2
print(" ".join(map(str,team.values())))
