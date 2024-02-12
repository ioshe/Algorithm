import sys
i = int(sys.stdin.readline().rstrip())
x=1
while x<i :
    if i-x == sum(list(map(int,str(x)))):
        print(x)
        exit()
    x+=1
print(0)