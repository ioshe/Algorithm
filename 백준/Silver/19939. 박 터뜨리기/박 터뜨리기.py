# https://www.acmicpc.net/problem/19939

from sys import stdin

N,K = map(int,stdin.readline().split())

min_required = K * (K + 1) // 2

if N < min_required:
    print(-1)
else:
    result = (K-1) + (1 if (N - min_required) % K else 0)
    print(result)



