from sys import stdin

N = int(stdin.readline())
result = []
for i in range(N) :
    N,A,D = map(int, stdin.readline().split())
    result.append((A*N)+(sum(range(1,N)) * D))
print('\n'.join(map(str,result)))