# https://www.acmicpc.net/problem/7785

from sys import stdin

n = int(stdin.readline())
records = list(map(lambda a: a.split(), stdin.read().splitlines()))
current = dict()

for name,log in records :
    if log == "leave" and current[name]:
        del(current[name])
    else :
        current[name] = 1

result = list(current.keys())
result.sort(reverse=True)
print("\n".join(result))
    