# https://www.acmicpc.net/problem/2083

from sys import stdin

a = stdin.read().splitlines()
result =[]
for text in a[:-1] :
    temp = text.split()
    result.append(f'{temp[0]} {"Senior" if (int(temp[1]) > 17 or int(temp[2]) >= 80) else "Junior"}')
print("\n".join(result))