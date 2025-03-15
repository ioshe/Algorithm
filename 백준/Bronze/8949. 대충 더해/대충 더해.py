a,b = input().split()
a = '0'*(len(b)-len(a)) + a
b = '0'*(len(a)-len(b)) + b
print(*list(int(i) + int(j) for i,j in (list(zip(a,b)))), sep='')