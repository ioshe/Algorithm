a,b = map(int,input().split())
mod_num = 2
min_result = 1
while mod_num<=a or mod_num <=b:
    if a%mod_num == 0 and b%mod_num == 0 :
        a//=mod_num
        b//=mod_num
        min_result*=mod_num
    else : 
        mod_num+=1
print(min_result)

if a==b :
    min_result = min_result*a
else :
    min_result = min_result*a*b

print(min_result)