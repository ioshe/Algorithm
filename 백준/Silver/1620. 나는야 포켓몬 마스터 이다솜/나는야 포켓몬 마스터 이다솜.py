#https://www.acmicpc.net/problem/1620
from sys import stdin
N,M = map(int,stdin.readline().split())
poket_list = {}
for _ in range(N):
    poket_list[stdin.readline().rstrip()] = _+1
reversed_dict = {value: key for key, value in poket_list.items()}
result=[]
for _ in range(M):
    a = stdin.readline().rstrip()
    if a.isdigit() :
        result.append(reversed_dict[int(a)])
    else :
        result.append(poket_list[a])
print("\n".join(map(str,result)))