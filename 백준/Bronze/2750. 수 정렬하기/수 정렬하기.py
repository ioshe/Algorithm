from sys import stdin
a = list(map(int,stdin.read().splitlines()[1:]))
a.sort()
print("\n".join(map(str,a)))
