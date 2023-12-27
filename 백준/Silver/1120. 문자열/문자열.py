#https://www.acmicpc.net/problem/1120
from sys import stdin
a,b = stdin.readline().split()
a = list(a)
len_list = []
for i in range(len(b) - len(a)+1) :
    hap = 0
    for j in range(len(a)) :
        if a[j] != b[i+j] :
            hap +=1
    len_list.append(hap)
print(min(len_list))