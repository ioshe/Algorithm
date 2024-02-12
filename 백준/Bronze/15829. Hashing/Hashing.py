# https://www.acmicpc.net/problem/15829
import sys
input = sys.stdin.readline
l = int(input().rstrip())
alpha = list(input().rstrip())
result = 0
for i in range(l):
    result += (ord(alpha[i])-96)*(31**i)
print(result % 1234567891)