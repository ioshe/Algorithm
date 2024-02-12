dohwagi = list(list(0 for i in range(0,100+1)) for i in range(0,100+1))
for _ in range(int(input())) :
    row,col = map(int,input().split())

    for i in range(row,row+10) :
        for j in range(col,col+10) :
            dohwagi[i][j] = 1
total = 0
for ch in (dohwagi):
    total += sum(ch)

print(total)