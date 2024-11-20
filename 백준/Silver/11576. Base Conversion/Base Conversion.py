# https://www.acmicpc.net/problem/11576

from sys import stdin

A,B = map(int,stdin.readline().split())
m = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))[::-1]

hap = 0
result = []

for i in range(m) :
    hap+= A**i * nums[i]

while hap > 0:
    temp = hap%B
    hap = hap//B
    result.append(temp)

print(*result[::-1])