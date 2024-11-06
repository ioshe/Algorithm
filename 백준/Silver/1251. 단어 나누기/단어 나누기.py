# https://www.acmicpc.net/problem/1251

from sys import stdin 

word = stdin.readline().strip()[::-1]

N = len(word)

result = "z" * 50
for i in range(1,N - 1) :
    for j in range(i+1, N) :
        result = sorted([word[j:] + word[i:j] + word[0:i],result])[0]

print(result)