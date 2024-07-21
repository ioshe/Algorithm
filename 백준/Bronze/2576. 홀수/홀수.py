# https://www.acmicpc.net/problem/2576
import sys
input = sys.stdin.read
data = list(map(int, input().split()))
odds = [x for x in data if x % 2]
print(f"{sum(odds)}\n{min(odds)}" if odds else -1)

