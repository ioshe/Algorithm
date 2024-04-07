# https://www.acmicpc.net/problem/1440

solution = input().split(":")

result = 0
for i in solution :
    if int(i) > 59 :
        result = 0
        break
    if 1<=int(i)<=12 :
        result+=2
    

print(result)