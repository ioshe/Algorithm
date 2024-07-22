# https://www.acmicpc.net/problem/2493

import sys 
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
result = [0 for i in range(n)]
stack = []
for i in range(n-1,0 - 1,-1) :
    while stack and stack[-1][0] < nums[i] :
        num, index = stack.pop()
        result[index] = i + 1
    else :
        stack.append((nums[i],i))
print(" ".join(map(str,result)))