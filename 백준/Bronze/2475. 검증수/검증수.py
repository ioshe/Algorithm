import sys
input = sys.stdin.readline
num = list(map(int,input().rstrip().split()))
result = 0
for i in num :
    result += i**2
print(result%10)