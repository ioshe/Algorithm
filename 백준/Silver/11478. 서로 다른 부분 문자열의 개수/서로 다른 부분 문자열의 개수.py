# https://www.acmicpc.net/problem/11478

a= input()

dupli = set()
for i in range(len(a)) :
    for j in range(i,len(a)) :
        dupli.add(a[i:j+1])
print(len(dupli))
# print(dupli)