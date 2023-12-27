#https://www.acmicpc.net/problem/1120
from sys import stdin
a,b = stdin.readline().split()
result=51 # max _value
for i in range(len(b) - len(a)+1) :
    hap = 0
    for j in range(len(a)) :
        if a[j] != b[i+j] :
            hap +=1
    if result > hap:
        result = hap
print(result)