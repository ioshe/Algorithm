# https://www.acmicpc.net/problem/1816

def check(num,sosu_list) :
    for j in sosu_list :
        if num % j == 0 :
            return False
    return True

from sys import stdin

MAX_VALUE = 10 ** 6
n = int(stdin.readline())
sosu = list(True for i in range(MAX_VALUE + 1))

for i in range(2,int(MAX_VALUE ** (1/2)) + 1) :
    for j in range(i*2,MAX_VALUE,i) :
        if sosu[j] : 
            sosu[j] = False

sosu_list = []
for i in range(2,MAX_VALUE) :
    if sosu[i] :
        sosu_list.append(i)

for i in range(n) :
    num = int(stdin.readline())
    if check(num,sosu_list) :
        print("YES")
    else :
        print("NO")
    