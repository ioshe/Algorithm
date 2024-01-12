# https://www.acmicpc.net/problem/1015

from sys import stdin

n = int(stdin.readline())
p = list(map(int,stdin.readline().split()))
sort_p = sorted(p)
new_list = []
for i in p :
    index = sort_p.index(i)
    new_list.append(index)
    sort_p[index] = -1
    
print(" ".join(map(str,new_list)))