# https://www.acmicpc.net/problem/2953
from sys import stdin

scores = list(map(lambda a : sum(list(map(int,a.split()))),stdin.read().splitlines()))

max = 0
for index,value in enumerate(scores) :
    if max < value :
        i = index
        max = value

print(i+1,max)