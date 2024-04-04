#https://www.acmicpc.net/problem/2738
I = lambda : map(int,(input().split()))
row,col = I()
a =[]
b = []
for _ in range(row):
    a.append(list(I()))
for _ in range(row):
    b.append(list(I()))

total = []
sub_total = []
for i in range(row) :
    for j in range(col) :
        sub_total.append(a[i][j]+b[i][j])
    total.append(sub_total)
    sub_total =[]

for i in range(row) :
    print(*total[i])