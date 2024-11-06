# https://www.acmicpc.net/problem/1251

from sys import stdin 

word = stdin.readline().strip()[::-1]

N = len(word)

result = "z" * 50
for i in range(N - 2) :
    for j in range(i+2, N) :
        result = sorted([word[j:] + word[i+1:j] + word[0:i+1],result])[0]

print(result)