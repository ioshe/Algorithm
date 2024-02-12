import sys
n = int(sys.stdin.readline().rstrip())
if n == 1 :
    print(1)
elif n <=7 :
    print(2)
else :
    six_n=[0,0,1]
    count = 2
    while True :
        if (n-2)//6 <six_n[count] :
            print(count)
            break
        six_n.append(six_n[count]+(six_n[count]-six_n[count-1])+1)
        count+=1