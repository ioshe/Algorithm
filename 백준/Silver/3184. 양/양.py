# https://www.acmicpc.net/problem/3184



import sys
from sys import stdin
sys.setrecursionlimit(10**6)


r,c = map(int, stdin.readline().split())
fields = list(map(lambda a: " ".join(a).split(), stdin.readlines()))

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(i,j,o,v):
    global r, c, fields

    for x,y in direction:
        if 0 <= i+x < r and 0 <= j+y < c and fields[i+x][j+y] != "#":
            if fields[i+x][j+y] == "o":
                o += 1
            elif fields[i+x][j+y] == "v":
                v += 1
            fields[i+x][j+y] = "#"
            o,v = dfs(i+x,j+y,o,v)
    return o,v


o,v = 0,0
for i in range(r):
    for j in range(c):
        if fields[i][j] != "#":
            if fields[i][j] == "o":
                fields[i][j] = "#"
                t_o, t_v = dfs(i,j,1,0)
            elif fields[i][j] == "v":
                fields[i][j] = "#"
                t_o, t_v = dfs(i,j,0,1)
            else:
                fields[i][j] = "#"
                t_o, t_v = dfs(i,j,0,0)
            # print(t_o,t_v)
            if t_o > t_v:
                o += t_o
            else:
                v += t_v
print(o,v)