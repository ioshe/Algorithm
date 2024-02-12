import sys
input = sys.stdin.readline
n = int(input()) 
end = len(str(n))
result = 0

for i in range(0,end) :
    sum = 10**(i+1) - (10**i)
    if sum-n<0 :
        result +=sum*(i+1)
        n = n-sum
    else :
        result +=n*(i+1)
print(result)