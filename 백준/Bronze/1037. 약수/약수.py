# https://www.acmicpc.net/problem/1037
input()
a=sorted(list(map(int,input().split())))
print(a[0]*a[-1])