#https://www.acmicpc.net/problem/1654
from sys import stdin
#랜선의 개수 K, 필요한 랜선의 개수 N
#1<=K<=10000 , 1<=N<=1,000,000 K ≦ N 
k,n = map(int,stdin.readline().rstrip().split()) 
wire_list = []
for i in range(k) :
    wire_list.append(int(stdin.readline().rstrip()))

first,last = 1,sum(wire_list)//n-1

while first<=last :
    midpoint=(first+last)//2
    sum=0
    for i in range(k):
        sum+=wire_list[i]//(midpoint+1)
    if sum >= n :
        first = midpoint+1
    else :
        last = midpoint-1
print(first)