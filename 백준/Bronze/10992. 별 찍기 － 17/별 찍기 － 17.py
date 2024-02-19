n = int(input())


for i in range(1,n+1) :
    if i == 1 :
        print(" "*(n-1)+"*")
        continue
    if i == n :
        print("*"*(2*n-1))
        continue
    print(" "*(n-i)+"*"+" "*(2*i-3)+"*")
    