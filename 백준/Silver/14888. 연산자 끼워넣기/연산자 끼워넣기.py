# https://www.acmicpc.net/problem/13251
from sys import stdin
n = int(stdin.readline())
nums = list(map(int,stdin.readline().split()))
operators = list(map(int,stdin.readline().split()))
result = []
def dfs(idx,plus,minus,multi,divide,sum) :
    if idx >= n :
        result.append(sum)
        return    
    else :
        if plus :
            dfs(idx+1,plus-1,minus,multi,divide,sum+nums[idx])
        if minus :
            dfs(idx+1,plus,minus-1,multi,divide,sum-nums[idx])
        if multi :
            dfs(idx+1,plus,minus,multi-1,divide,sum*nums[idx])
        if divide :
            dfs(idx+1,plus,minus,multi,divide-1,int(sum / nums[idx]))
dfs(1,operators[0],operators[1],operators[2],operators[3],nums[0])
print(max(result))
print(min(result))