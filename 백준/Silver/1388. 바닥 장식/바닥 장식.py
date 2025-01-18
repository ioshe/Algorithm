# https://www.acmicpc.net/problem/1388

from sys import stdin

N,M = map(int,stdin.readline().split())
texts = list(map(lambda a : a.strip(),stdin.readlines()))
overlap = 0

visited = [[1 for _ in range(N)] for __ in range(M)]
for i in range(N):
    for j in range(M):
        if texts[i][j] == "-" and j+1 < M and texts[i][j+1] == "-":
            overlap += 1
            continue
        if texts[i][j] == "|" and i+1 < N and texts[i+1][j] == "|":
            overlap += 1
            continue

print(N * M - overlap)
            
            