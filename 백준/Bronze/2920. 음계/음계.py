#https://www.acmicpc.net/problem/2920
import sys
num = list(map(int,sys.stdin.readline().rstrip().split()))
result = ["ascending","descending","mixed"]
index_ = num.index(1)
is_result = True
count = 1

if num == sorted(num) :
    print(result[0])
    exit()
while count<=7 :
    if num[index_] > num[index_-1] :
        is_result = False
        break
    count+=1
    index_-=1
if is_result :
    print(result[1])
else :
    print(result[2])
        