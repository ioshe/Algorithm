# https://www.acmicpc.net/problem/17521

from sys import stdin

n,w = map(int,stdin.readline().split())
queue = list(map(int,stdin.readlines()))

i = 1
lower = queue[0]
while i < n:
    if lower < queue[i]:
        count = w // lower 
        w += (queue[i] - lower) * count
    lower = queue[i]
    i += 1

print(w)