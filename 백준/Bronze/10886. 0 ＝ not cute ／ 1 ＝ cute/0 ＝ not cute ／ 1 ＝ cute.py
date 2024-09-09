# https://www.acmicpc.net/problem/10886

from sys import stdin

n = int(stdin.readline())
cute = sum(map(int,stdin.readlines()))
if cute > n//2 :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
