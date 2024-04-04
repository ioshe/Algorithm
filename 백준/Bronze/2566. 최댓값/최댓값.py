a =[]
for _ in range(9) :
    a.append(list(map(int,(input().split()))))
a=sum(a,[])
index = a.index(sorted(a)[-1])
print(sorted(a)[-1])
print(index//9+1,index%9+1)
