#https://www.acmicpc.net/problem/11659
from sys import stdin
N,M = map(int,stdin.readline().split())
nums = [0] + list(map(int,stdin.readline().split()))
result = []
for k in range(1,N+1) :
    nums[k] +=  nums[k-1] 
for _ in range(M) :
    i,j = map(int,stdin.readline().split())
    result.append(nums[j]-nums[i-1])

print("\n".join(map(str,result)))