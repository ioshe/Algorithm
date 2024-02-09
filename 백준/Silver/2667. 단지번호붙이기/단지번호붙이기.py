from sys import stdin
n = int(stdin.readline())
graph = [list(map(int," ".join(stdin.readline()).split())) for _ in range(n)]
moving = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(target,queue) :
    global graph,n,moving
    count = 1
    while queue :
        i,j= queue.pop(0)
        for x,y in moving :
            nx,ny = i+x,j+y
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 0 :
                graph[nx][ny] = 0
                queue.append((nx,ny))
                count +=1 

    return count

result = []
for i in range(n) :
    for j in range(n) :
        if graph[i][j] != 0 :
            graph[i][j]= 0
            result.append(bfs(graph[i][j],[(i,j)]))
result.sort()
print(len(result))
print("\n".join(map(str,result)))