# https://www.acmicpc.net/problem/2154
def sol(n) :
    result = ""
    for i in range(1,n+1) :
        result += str(i)
    return result.find(str(n))

n = int(input())
print(sol(n)+1)

