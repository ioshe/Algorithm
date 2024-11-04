# https://www.acmicpc.net/problem/9625

from sys import stdin

n = int(stdin.readline())

if n == 1 :
    print(0,1)
else :
    pibonacchi = [0,1,1]
    for i in range(2,n) :
        pibonacchi.append(pibonacchi[i]+pibonacchi[i-1])
    print(pibonacchi[n-1],pibonacchi[n])