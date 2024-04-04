
a =[]
for _ in range(5) :
    a.append(list(input()))

for j in range(15) :
    for i in range(5) :
        try : 
            print(a[i][j],end="")
        except :
            continue