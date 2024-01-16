a,b = map(int,input().split())
result = []
for i in range(1,a*b+1) :
    if not(i%b) and not(i%a) :
        result.append(3)
    elif not(i%a) :
        result.append(2)
    elif not(i%b) :
        result.append(1)

print("".join(map(str,result)))