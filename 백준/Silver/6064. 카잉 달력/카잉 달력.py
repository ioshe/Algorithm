import sys
def cal_num(a,b) :
    if b>a :
        a,b=b,a
    while b:
        a,b=b,a%b
    return a

input = sys.stdin.readline
for _ in range(int(input().rstrip())) :
    m,n,x,y = map(int,input().rstrip().split())
    i = 1
    a=cal_num(m,n)
    if (m%2==0 and n%2==0 and (x+y)%2) :
        print(-1)
        continue
    while i<=m*n//a :
        if (i-x)%m==0 :
            break
        i+=1
    while i<=m*n//a :
        if (i-y)%n==0:
            break
        i+=m    
    
    if i<=m*n//a :
        print(i)    
    else :
        print(-1)