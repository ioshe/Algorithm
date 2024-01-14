# https://www.acmicpc.net/problem/21921
from sys import stdin
n,x = map(int,stdin.readline().split())
visited = list(map(int,stdin.readline().split()))
first_hap = sum(visited[:x])
nums = [first_hap]
for i in range(len(visited)-x) :
    first_hap += visited[i+x]-visited[i]
    nums.append(first_hap)
    
#nums.append(first_hap)
top_value = max(nums)
if top_value == 0 :
    print("SAD")
else :
    print(top_value)
    print(nums.count(top_value))
