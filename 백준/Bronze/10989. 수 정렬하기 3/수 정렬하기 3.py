import sys
input = sys.stdin.readline
num_max = 10001
num = [0]*num_max
for i in range(int(input().rstrip())) :
    num[int(input().rstrip())] +=1
for i in range(10001):
    if num[i] >= 1:
        for j in range(num[i]) :
            print(i)