from sys import stdin
result = []
while True :
    n = int(input())
    if n == 0 :
        break

    name_list = [stdin.readline().strip() for i in range(n)]
    state_list = [0 for i in range(n)]
    for i in range(1,2*n) :
        num,a = stdin.readline().split()
        if state_list[int(num)-1] == 1:
            state_list[int(num)-1] -=1
        else :
            state_list[int(num)-1]+=1
    
    for i in range(0,n) :
        if state_list[i] == 1 :
            result.append(name_list[i])

for index,value in enumerate(result) :
    print(index+1,value)