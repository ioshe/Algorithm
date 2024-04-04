deep = int(input()) #1 ≤ N ≤ 100

for i in range(1,deep+1) :
    print(" "*(deep-i),end="")
    print("*"*(i*2-1))
for i in range(deep-1,0,-1) :
    print(" "*(deep-i),end="")
    print("*"*(i*2-1))