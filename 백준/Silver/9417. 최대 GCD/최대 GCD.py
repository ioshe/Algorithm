# https://www.acmicpc.net/problem/9417

from sys import stdin
from itertools import combinations

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(stdin.readline())
result = []
for _ in range(n):
    nums = list(map(int, stdin.readline().split()))
    max_gcd = 0
    for a, b in combinations(nums, 2):
        max_gcd = max(max_gcd, gcd(a, b))
    result.append(max_gcd)

print('\n'.join(map(str, result)))