from sys import stdin
i=0
num = int(stdin.readline().rstrip())
while num-2**i>0:
    i+=1
print(2**i-(2**i-num)*2)