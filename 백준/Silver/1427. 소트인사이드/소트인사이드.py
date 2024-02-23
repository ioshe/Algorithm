# https://www.acmicpc.net/problem/1427
n = input()
print("".join(sorted(" ".join(n).split(" "),reverse=True)))

