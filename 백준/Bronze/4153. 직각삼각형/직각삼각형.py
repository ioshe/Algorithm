import sys
input = sys.stdin.readline

a,b,c = map(int,input().rstrip().split())
while True :
    if max(a,b,c) == a :
        c,a,b = a,b,c
    elif max(a,b,c) == b:
        c,a,b = b,a,c
    if a ==0 or b== 0 or c==0 :
        break
    elif c**2 == (a**2+b**2) :
        print("right")
    else :
        print("wrong")
    a,b,c = map(int,input().rstrip().split())