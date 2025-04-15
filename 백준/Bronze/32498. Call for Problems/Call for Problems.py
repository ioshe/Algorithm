from sys import stdin

print(sum(1 if i %2 == 1 else 0 for i in list(map(int,stdin.readlines()[1:]))))