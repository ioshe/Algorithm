n = int(input())

for i in range(1,n+1) :
    starts = "* "*(n-1)+"*"
    if not i%2 :
        print(" "+starts)
    else :
        print(starts)