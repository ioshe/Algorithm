# https://www.acmicpc.net/problem/26517

x = int(input())
a,b,c,d = map(int,input().split())

if (x*(a-c) == -b + d):
    print(f"Yes {a*x+b}")
else :
    print(f"No")