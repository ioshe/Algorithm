# https://www.acmicpc.net/problem/2010
from sys import stdin
a = stdin.read().splitlines()
a= list(map(int,a[1:]))
print(sum(a)-len(a)+1)