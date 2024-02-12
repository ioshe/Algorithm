from sys import stdin
n,k= map(int,stdin.readline().split())
result = [True for _ in range(n+1)]
for i in range(2,n+1) :
    if result[i] :
        #print(i,"번쨰 ",result[i])
        for j in range(i,n+1,i):
            if result[j] :
                result[j] = False
                #print(k," : ",j)
                k-=1
                if k == 0:
                    print(j)
                    exit(0)