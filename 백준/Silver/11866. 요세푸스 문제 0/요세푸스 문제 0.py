from sys import stdin
n,k = map(int,stdin.readline().split())
n_bool = [True for i in range(n)]
result = []
i=k-1
while True:
    if n_bool[i] :
        n_bool[i] = False
        result.append(str(i+1))
    if len(result) == len(n_bool) :
        break
    count = 0
    while count != k :
        count +=1
        i= (i+1)%n
        while n_bool[i] == False :
            i= (i+1)%n
        

print(f'<{", ".join(map(str,result))}>')