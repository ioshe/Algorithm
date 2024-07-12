# https://www.acmicpc.net/problem/2490
for i in range(3) :
    temp = 4 - sum(map(int,input().split()))
    if temp == 0 :
        print("E")
        continue
    print(chr(temp+64))