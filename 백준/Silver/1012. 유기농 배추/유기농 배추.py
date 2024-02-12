#https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10 ** 5) 
dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(x,y) :
    # print()
    # print("\n".join(map(str,seed)))
    for i in range(4) :
        NX = x+dx[i]
        NY = y+dy[i]
        if NX<=-1 or NX>=M or NY<=-1 or NY>= N :
            continue
        if seed[NX][NY] == 0 :
            continue
        seed[NX][NY] = 0
        bfs(NX,NY)

for _ in range(int(sys.stdin.readline())) :
    M,N,K = map(int,sys.stdin.readline().split())
    seed = [[0 for i in range(N)] for j in range(M)]
    for i in range(K) :
        a,b = map(int,sys.stdin.readline().split())
        seed[a][b] = 1

    result = 0
    for i in range(M) :
        for j in range(N) :
            if seed[i][j] == 1:
                bfs(i, j)
                result += 1
            
    print(result)