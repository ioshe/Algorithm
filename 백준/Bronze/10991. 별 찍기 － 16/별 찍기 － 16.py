n = int(input())

result = []
for i in range(1,n+1) :
    if i == 1 :
        temp = " "*(n-i) + "*"
    else :
        temp = " "*(n-i) + "* "*(i-1)+"*"
    result.append(temp)
print("\n".join(result))