# https://www.acmicpc.net/problem/2493

import sys 
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
result = [0 for i in range(n)]
stack = []

for i in range(n) :
    while stack and nums[stack[-1]] < nums[i] :
        stack.pop()
    if stack : 
        result[i] = stack[-1] + 1
    stack.append(i)
print(" ".join(map(str,result)))