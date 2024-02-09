#https://www.acmicpc.net/problem/11047
import sys
n,k = map(int,sys.stdin.readline().split())
n_values = list(map(int,sys.stdin.read().splitlines()))
sum=0
for i in range(n-1,0-1,-1) :
    if k == 0 :
        break
    if k% n_values[i] < k :
        sum+=k//n_values[i]
        k%=n_values[i]
print(sum)