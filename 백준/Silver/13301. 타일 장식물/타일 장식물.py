#https://www.acmicpc.net/problem/13301
rect = [1,1,2,3,5]
squre = [4, 6, 10, 16, 26]
n =int(input())
for i in range(5,n) :
    rect.append(rect[i-4]+rect[i-3]+rect[i-1])
    squre.append(squre[i-1]+rect[i]*2)
print(squre[n-1])