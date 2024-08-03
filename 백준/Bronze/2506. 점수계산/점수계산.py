# https://www.acmicpc.net/problem/2506

'''
10
1 0 1 1 1 0 0 1 1 0
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
result = count = 0
for i in nums :
    if i == 1 :
        count += 1
        result += count 
    else :
        count = 0
print(result)