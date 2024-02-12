#https://www.acmicpc.net/problem/1010
from sys import stdin
MAX = 30
num_sequence = [0,1]
for i in range(2,MAX+1):
    num_sequence.append(num_sequence[i-1]*i)
result = []
for _ in range(int(stdin.readline())) :
    b,a = map(int,stdin.readline().split())
    if a == b :
        result.append(1)
    else :
        result.append(num_sequence[a]//((num_sequence[a-b]*num_sequence[b])))

print("\n".join(map(str,result)))