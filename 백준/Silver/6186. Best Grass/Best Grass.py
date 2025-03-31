# https://www.acmicpc.net/problem/6186
import sys
from sys import stdin

sys.setrecursionlimit(10**6)
R,C = map(int,stdin.readline().split())
board = [list(stdin.readline().rstrip()) for _ in range(R)]
answer = 0


def dfs(r,c):
    global answer
    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr,nc = r+dr,c+dc
        if 0<=nr<R and 0<=nc<C and board[nr][nc] == '#':
            board[nr][nc] = '.'
            dfs(nr,nc)

for i in range(R):
    for j in range(C):
        if board[i][j] == '#':
            board[i][j] = '.'
            answer += 1
            dfs(i,j)

print(answer)