#https://www.acmicpc.net/problem/1057
from sys import stdin
r,a,b = map(int,stdin.readline().split())
cnt = 0
while True :
    cnt +=1
    a = (a+1)//2
    b = (b+1)//2
    if a==b : 
        break
print(cnt)