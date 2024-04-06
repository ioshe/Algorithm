# https://www.acmicpc.net/problem/1371

from sys import stdin

lines = stdin.read().splitlines()

letters = {}

for i in (lines) :
    for j in i :
        # print(letters)
        if j == ' ' :
            continue
        if j not in letters :
            letters[j] = 1
        else :
            letters[j] += 1

mmax = max(letters.values())
result = []

for i in letters :
    if mmax == letters[i] :
        result.append(i)
# print(letters)
result.sort()
print("".join(map(str,result)))
