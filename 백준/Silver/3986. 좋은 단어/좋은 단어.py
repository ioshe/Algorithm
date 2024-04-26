# https://www.acmicpc.net/problem/3986
from sys import stdin

n = int(stdin.readline())
word = list(map(lambda a: a.strip(), stdin.readlines()))
count = 0

for i in range(n) :
    stack = []
    for w in word[i] :
        if stack and stack[-1] == w :
            stack.pop()    
            continue
        stack.append(w)
    if not stack:
        count += 1
print(count)