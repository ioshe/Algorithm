import sys

k = int(sys.stdin.readline().rstrip())
result = 1
for i in range(2,k+1) :
    result*=i
count = 0
for w in str(result)[::-1] :
    if w!='0' :
        print(count)
        break
    count +=1