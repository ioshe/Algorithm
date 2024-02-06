# 1312
a,b,n = map(int,input().split())
if n == 1 :
    print(int(a/b*10%10))
else :
    for i in range(n) :
        a = a * 10
        d = a // b
        a = a % b
    print(d)