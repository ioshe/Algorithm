# https://www.acmicpc.net/problem/5347


from sys import stdin

def gcd(a, b) -> int:
    if a > b :
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b

n = int(stdin.readline())
nums = list(map(lambda a : list(map(int, a.split())), stdin.readlines()))
for (x,y) in nums:
    print(x * y // gcd(x,y))
    