#https://www.acmicpc.net/problem/17213
f=[1 for i in range(0,31)]
for i in range(1,len(f)) :
	f[i] =f[i-1]*i
import sys
n,m = map(int,sys.stdin.read().splitlines())
N=m-1
M=n-1
#print(f[N+M-1]//(f[N-1]*f[M]))
print(f[N]//(f[N-M]*f[M]))