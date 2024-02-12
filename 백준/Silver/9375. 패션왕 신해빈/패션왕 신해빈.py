#https://www.acmicpc.net/problem/9375
from sys import stdin
mux = [i for i in range(30+1)]
for i in range(2,30+1) :
    mux[i]*= mux[i-1]

T = int(stdin.readline()) #testcase 
result=[]
for _ in range(T):
    dresses = dict()
    N = int(stdin.readline())
    for i in range(N) :
        value, key = stdin.readline().rstrip().split()
        dresses[key] = dresses.get(key,0) +1
    sum = 1
    for i in dresses :
        sum *= (dresses[i] +1)
    result.append(sum-1)

print("\n".join(map(str,result)))