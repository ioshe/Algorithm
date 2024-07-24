
from sys import stdin

print("\n".join(map(str,sorted(list(map(int,stdin.readlines()[1:])),reverse=True))))