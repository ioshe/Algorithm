from sys import stdin
a= list(map(int,stdin.read().splitlines()))
result = []
for num in a[:-1] :
    i =1
    sum_i=[]
    while i<num//2+1 :
        if num%i==0 :
            sum_i.append(i)
        i+=1
    
    if sum(sum_i)==num :
        print(num,"="," + ".join(map(str,sum_i)))
    else :
        print(num,"is NOT perfect.")