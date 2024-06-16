# https://www.acmicpc.net/problem/3135

from sys import stdin

A,B = map(int,stdin.readline().split())
N = int(stdin.readline())
frequ = list(map(int,stdin.readlines()))

frequ.sort(key = lambda a : abs(B-a))

print(min(abs(frequ[0] - B) + 1,abs(B-A)))
