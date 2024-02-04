#https://www.acmicpc.net/problem/2441

a,b = map(int,input().split())

a = list(map(int," ".join(str(a)).split()))
b = list(map(int," ".join(str(b)).split()))
result = 0
b = sum(b)
for i in a :
    result += i*b

print(result)