#https://www.acmicpc.net/problem/2217

from sys import stdin

li = list(map(int,stdin.read().splitlines()))[1:]
li.sort(reverse = True)
weight = 0
for i in range(len(li)) :
    temp = li[i] * (i + 1)
    weight = temp if weight < temp else weight

print(weight)

