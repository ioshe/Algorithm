from sys import stdin

n = int(stdin.readline())

word = [stdin.readline().split() for i in range(n)]

print("\n".join(" ".join(s[::-1] for s in w) for w in word))