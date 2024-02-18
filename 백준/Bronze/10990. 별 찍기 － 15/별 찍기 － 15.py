n = int(input())
for i in range(1,n+1) :
    if i == 1 :
        blank = " "*(n-i)
        print(blank + "*")
        continue
    left_blank = " "*(n-i)
    mid_blank = " "*(2*(i-1)-1)
    print(left_blank+"*"+mid_blank+"*")