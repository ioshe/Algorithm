
a=0
while True :
    try :
        a=int(input())
    except  :
        break
    num = 1
    while True :
        if num%a == 0 :
            print(len(list(map(int,str(num)))))
            break
        else :    
            num=num*10+1

