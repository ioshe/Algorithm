from sys import stdin

t = int(stdin.readline())
result = []
for i in range(t) :
    n,m = map(int,stdin.readline().split())
    for j in range(m) :
        stdin.readline()
    result.append(n-1)
print("\n".join(map(str,result)))