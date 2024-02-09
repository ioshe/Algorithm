from sys import stdin
n,*num_list = map(int,stdin.read().splitlines())
if n <= 1:
    print(num_list[0])
elif n == 2 :
    print(num_list[0]+num_list[1]) 
elif n == 3 :
    print(max(num_list[0],num_list[1])+num_list[2]) 
else :
    result = [0]*n
    result[0],result[1] = num_list[0],num_list[0]+num_list[1]
    result[2] = max(num_list[0],num_list[1])+num_list[2]
    for i in range(3,n) :
        result[i] = max(result[i-2],num_list[i-1]+result[i-3]) +num_list[i]
    print(result[n-1])