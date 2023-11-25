a = int(input())
b= int(input())

num = (a//100)*100
for i in range(num,num+99,1) :
    if i%b == 0 :
        break
print(f'{i-num:02d}')