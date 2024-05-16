n = int(input())
for i in range(n,0,-1) :
    null_t = " "*(n-i)
    print(null_t+"*"*(i*2-1))
for i in range(2,n+1) :
    null_t = " "*(n-i)
    print(null_t+"*"*(i*2-1))