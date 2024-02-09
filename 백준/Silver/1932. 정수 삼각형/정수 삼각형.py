#https://www.acmicpc.net/problem/1932
from sys import stdin
n = int(stdin.readline())
num_list = [[] for i in range(n)]
for _ in range(n) :
    num_list[_] = list(map(int,stdin.readline().split()))
    
for i in range(1,n) :
    length =len(num_list[i])
    for j in range(length) :
        if j == 0 :
            num_list[i][j] += num_list[i-1][0]
        elif j == length-1 :
            num_list[i][j] += num_list[i-1][-1]
        else :
            num_list[i][j] += max(num_list[i-1][j-1],num_list[i-1][j])

print(max(num_list[-1]))