from sys import stdin

n,m = map(int,stdin.readline().split())
graph = [list(map(int," ".join(stdin.readline()).split())) for _ in range(n)]
max_squre = min(n,m) # 제일 큰 정사각형은 가로 세로 중 작은값을 가진다.
temp = 0
for i in range(n) :
    for j in range(m) :
        limit = i if max_squre == n else j
        for k in range(temp,max_squre - limit) :
            if k+i >= n or k+j >= m :
                break       
            if graph[i][j] == graph[i+k][j] == graph[i][j+k] == graph[i+k][j+k] :
                if temp < k :
                    temp = k
print((temp+1)**2)
