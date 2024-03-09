# https://www.acmicpc.net/problem/2154

n = int(input())
result = ""
for i in range(1,n+1) :
    result += str(i)

print(result.find(str(n))+1)
