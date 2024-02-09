txt = input()
total = 0
for i in txt :
    if 'a'<=i <='z' :
        total+= ord(i)- 96
    else :
        total += ord(i) - 38
MAX = 1100
dp = [True for i in range(MAX+1)]
for i in range(2,int(MAX**0.5)+1) :
    for j in range(i*i,MAX+1,i):    
        if dp[j] :
            dp[j] = False

print("It is a prime word." if dp[total] else "It is not a prime word.")