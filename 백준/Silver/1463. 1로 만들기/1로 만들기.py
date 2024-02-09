# https://www.acmicpc.net/problem/1463
n = int(input())
num_list = [0]*(1000000+1)
num_list[1],num_list[2],num_list[3] = 0,1,1
if n>3 :
    for i in range(4,n+1) :
        ans = num_list[i-1]+1
        if i%3 == 0:
            ans = min(ans,num_list[i//3]+1)
        if i%2 == 0:
            ans = min(ans,num_list[i//2]+1)
        num_list[i] = ans
print(num_list[n])