# https://www.acmicpc.net/problem/21921
from sys import stdin
n,x = map(int,stdin.readline().split())
visited = list(map(int,stdin.readline().split()))
first_hap = sum(visited[:x])
cnt,max_val = 1,first_hap
for i in range(n-x) :
    first_hap += visited[i+x]-visited[i]
    if max_val < first_hap :        
        cnt = 1
        max_val = first_hap
    elif max_val == first_hap :
        cnt +=1
    
#nums.append(first_hap)
if max_val == 0 :
    print("SAD")
else :
    print(max_val)
    print(cnt)