# https://www.acmicpc.net/problem/13413

from sys import stdin

t = int(stdin.readline())
result = []

for _ in range(t): 
    n = int(stdin.readline())
    start = stdin.readline().strip()
    end = stdin.readline().strip()
    diffrent = {"W":0,"B":0}
    for i in range(len(start)):
        if start[i] != end[i]:
            diffrent[start[i]]+=1
    result.append(max(diffrent.values()))
print("\n".join(map(str,result)))  