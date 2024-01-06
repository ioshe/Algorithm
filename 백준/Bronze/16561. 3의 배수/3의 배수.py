n = int(input())

count = 0
for i in range(3,n-6+1,3) :
    for j in range(3,n-3-i+1,3) :
        if (n-i-j) //3 :
            count +=1
print(count)
        
