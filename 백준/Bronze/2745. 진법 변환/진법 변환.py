a,b=input().split()
jinsu = int(b)
total = 1

for index,te in enumerate(a[::-1]) :
    if te.isdigit() :
        total += int(te) * (jinsu**index )
    else :
        total += (jinsu**index) * (ord(te)-ord('A')+10)
print(total-1)