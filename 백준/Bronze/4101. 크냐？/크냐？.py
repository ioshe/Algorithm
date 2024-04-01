from sys import stdin

a = list(map(lambda a : tuple(map(int,a.split())) , stdin.read().splitlines()))
print("\n".join(["Yes" if i > j else "No" for i, j in a[:-1]]))