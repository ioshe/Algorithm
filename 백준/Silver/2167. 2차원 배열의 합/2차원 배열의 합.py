#https://www.acmicpc.net/problem/2167
from sys import stdin

N,M = map(int,stdin.readline().split())
nums = [list(map(int,stdin.readline().split())) for i in range(N)]
haps = []
for i in range(N) :
    temp = []
    for j in range(M) :
        temp.append(sum(nums[i][:j+1]))
    haps.append(temp)

K = int(stdin.readline())
for i in range(K) :
    i,j,x,y = map(int,stdin.readline().split())
    h = 0
    for p in range(i-1,x) :
        h +=(haps[p][y-1]-sum(nums[p][0:j-1]))
    print(h)