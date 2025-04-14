# https://www.acmicpc.net/problem/18511

from sys import stdin
from itertools import product

n, k = stdin.readline().split()
elements = list(map(int, stdin.readline().split()))
elements.sort(reverse=True)
result = 0

def get_nums(elements, n):
    for i in product(elements, repeat=n):
        yield int("".join(map(str,i)))

# 주어진 수에서 가장 큰 자릿수가 elements의 가장 작은수보다 작으면 자릿수를 하나 내려야한다.
if int(n[0]) <= elements[-1]:
    cal_len = len(n) - 1
else:
    cal_len = len(n)

for i in get_nums(elements, cal_len):
    # print(i)
    if i <= int(n):
        result = max(result, i)


print(result)