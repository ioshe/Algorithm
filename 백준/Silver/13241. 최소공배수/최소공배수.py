def gcd(a,b) :
    (a,b) = (a,b) if a > b else (b,a)
    while b > 0 :
        a,b = b,a%b 
    return a


A,B = map(int,input().split())
n = gcd(A,B)
print((A*B)//n)
