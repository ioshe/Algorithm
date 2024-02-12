#https://www.acmicpc.net/problem/11060
from sys import stdin

n = int(stdin.readline())
maze = [*map(int,stdin.readline().split())]
dp = [10000]*n
dp[0]=0
for i in range(0,n) :
	for j in range(i,i+maze[i]+1) :
		if j < len(maze) :
			dp[j] = min(dp[j],dp[i]+1)
if dp[-1] != 10000 :
	print(dp[-1])
else :
	print(-1)