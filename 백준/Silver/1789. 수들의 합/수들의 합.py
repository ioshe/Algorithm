# https://www.acmicpc.net/problem/1789

def find_max(S) :
    n = 1
    while n * (n + 1) / 2 <= S:
        n += 1
    return n - 1
S = int(input())
print(find_max(S))