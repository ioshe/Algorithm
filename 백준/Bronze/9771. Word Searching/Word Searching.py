# https://www.acmicpc.net/problem/9771

from sys import stdin

word = stdin.readline().strip()
texts = stdin.readlines()

print(sum(map(lambda text : text.count(word), texts)))