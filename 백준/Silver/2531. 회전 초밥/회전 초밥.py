# https://www.acmicpc.net/problem/2531

'''
8 30 4 30
7
9
7
30
2
7
9
25
'''

from sys import stdin
from collections import deque
N,d,k,c = map(int,stdin.readline().split())
data = list(map(int,stdin.readlines()))
#dp = [0] * N
result = 0
# 끝에 이어서 하기 위한 거
temp = data[N-k+1:] + data[0:k-1]
for i in range(0,N - k + 1) :
    result = max(result, len(set(data[i:i+k])) + (1 if c not in data[i:i+k] else 0))
    #dp[i] = len(set(data[i:i+k])) + (1 if c not in data[i:i+k] else 0)
for i in range(k-1) :
    result = max(result, len(set(temp[i:i+k])) + (1 if c not in temp[i:i+k] else 0))
    #dp[i+k+1] = len(set(temp[i:i+k])) + (1 if c not in temp[i:i+k] else 0)
print(result)
# print(dp)