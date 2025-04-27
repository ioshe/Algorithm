# https://www.acmicpc.net/problem/5568

from sys import stdin
from itertools import permutations

n = int(stdin.readline())
k = int(stdin.readline())

nums = list(map(int,stdin.readlines()))

print(len(set("".join(map(str,i)) for i in permutations(nums,k))))

