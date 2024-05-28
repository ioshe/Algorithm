# https://www.acmicpc.net/problem/10815

'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''

from sys import stdin

n = int(stdin.readline())
in_nums = set(map(int,stdin.readline().split()))
m = int(stdin.readline())
find_nums = list(map(int,stdin.readline().split()))

result = []
for i in find_nums :
    if i in in_nums :
        result.append(1)
    else :
        result.append(0)

print(" ".join(map(str,result)))
