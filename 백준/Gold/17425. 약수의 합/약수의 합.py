# # https://www.acmicpc.net/problem/17425
import sys
input = sys.stdin.readline

LIMIT = 1000001
second_list = [1 for i in range(LIMIT)]

for i in range(2,LIMIT) :
    j=1
    while(i*j<LIMIT) :
        second_list[i*j] += i
        j+=1 
    second_list[i] += second_list[i-1] 

n = int(input().rstrip())    
for _ in range(n) :
    a=int(input().rstrip())
    sys.stdout.write(str(second_list[a])+"\n")