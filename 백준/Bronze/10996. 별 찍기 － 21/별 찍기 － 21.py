# https://www.acmicpc.net/problem/10996
n = int(input())
result = []
if n == 1 :
    print("*")
else :
    for i in range(n*2) :
        temp = []
        for j in range(n) :
            if (j+i)%2 :
                temp.append(" ")
            else :
                temp.append("*")
        result.append(temp)
    print("\n".join("".join(re) for re in result))