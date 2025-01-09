# https://www.acmicpc.net/problem/20291

from sys import stdin

result = {}

for line in stdin.readlines()[1:]:
    key = line.strip().split(".")[1]
    result[key] = result.get(key, 0) + 1

print("\n".join(f"{re} {result[re]}" for re in sorted(list(result.keys()))))