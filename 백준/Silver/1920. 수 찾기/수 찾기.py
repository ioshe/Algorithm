# https://www.acmicpc.net/problem/1920
from sys import stdin
def binary_search(i,n_list) :
    start=0
    end = len(n_list)-1
    while start <= end :
        midpoint = (start+end)//2
        if i == n_list[midpoint] :
            return '1'
        elif i > n_list[midpoint]:
            start = midpoint+1 
        else :
            end = midpoint-1
    return '0'

n = int(stdin.readline().rstrip())
#n_list = list(set(map(int,stdin.readline().rstrip().split())))
n_list = sorted(set(map(int,stdin.readline().rstrip().split())))
m = int(stdin.readline().rstrip())
m_list = list(map(int,stdin.readline().rstrip().split()))
result = []
for i in m_list :
    result.append(binary_search(i,n_list))

print("\n".join(result)) 
