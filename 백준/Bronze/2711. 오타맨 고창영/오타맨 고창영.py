t = int(input())

for i in range(t) :
    n,text = input().split()
    print(text[:int(n)-1]+text[int(n):])