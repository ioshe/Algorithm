# https://www.acmicpc.net/problem/2386
from sys import stdin

s = list(map(lambda a: a.split(),stdin.readlines()[:-1]))

for i in s :
    print(i[0]," ".join(i[1:]).lower().count(i[0]))

