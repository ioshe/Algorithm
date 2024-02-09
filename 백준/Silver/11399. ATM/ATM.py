#https://www.acmicpc.net/problem/11399
from sys import stdin

n = int(stdin.readline())
num_list = list(map(int,stdin.readline().rstrip().split()))
num_list.sort()
sum=num_list[0]
for i in range(1,len(num_list)) :
    num_list[i] = num_list[i-1]+num_list[i]
    sum+=num_list[i]
print(sum)