# https://www.acmicpc.net/problem/10825

from sys import stdin

n = int(stdin.readline())
names = {}
scores = []
for i in range(n) :
    temp = stdin.readline().split()
    scores.append([temp[0],list(map(int,temp[1:]))])

scores.sort(key= lambda a:(-a[1][0],a[1][1],-a[1][2],a[0]))
print("\n".join(i[0] for i in scores))