# https://www.acmicpc.net/problem/14490

from sys import stdin

def gcd(a, b):
    reverse = False
    if a < b : 
        a,b = b,a
        reverse = True
    while b > 0 :
        a,b = b, a % b
    return a
n,m = map(int,stdin.readline().split(":"))

temp = gcd(n,m)
print(f"{n//temp}:{m//temp}")
