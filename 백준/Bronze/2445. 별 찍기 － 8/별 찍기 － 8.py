n = int(input())

li = n*2
for i in range(1,n+1) :
    print("*"*i+" "*(li-i*2)+"*"*i)
for i in range(n-1,0,-1) :
    print("*"*i+" "*(li-i*2)+"*"*i)