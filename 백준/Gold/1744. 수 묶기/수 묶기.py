# https://www.acmicpc.net/problem/1744

from sys import stdin

n = int(stdin.readline())
plus = []
minus = []
hap = 0
for i in map(int,stdin.readlines()) :
    if i > 1 :
        plus.append(i)
    elif i == 1 :
        hap += 1 # 1은 묶지 않는게 더 좋음
    else :
        minus.append(i)

plus.sort()
minus.sort(reverse=True)
x = 0
while len(plus) >= 2 :
    a = plus.pop()
    b = plus.pop()
    hap += a * b 

while len(minus) >= 3 :
    a = minus.pop()
    b = minus.pop()
    hap += a * b 

if len(plus) == 1 :
    hap += plus[0]

if len(minus) == 1 :
    print(hap + minus[0])
#elif 0 in minus :
elif len(minus) == 2: 
    print(hap + minus[0] * minus[1])
else :
    print(hap)