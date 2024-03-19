#https://www.acmicpc.net/problem/5988
from sys import stdin
print("\n".join(["odd" if i%2 else "even" for i in map(int,stdin.read().splitlines()[1:])]))