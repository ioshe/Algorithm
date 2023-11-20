n=int(input())
fibonacchi = [1,1,1]
for i in range(3,n):
    fibonacchi.append(fibonacchi[i-1]+fibonacchi[i-3])
print(fibonacchi[n-1])