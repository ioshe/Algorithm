import sys
input = sys.stdin.readline

max = 1001
num_list = [True for i in range(max)]

num_list[0],num_list[1] = False, False
limit = int(max**0.5)
for i in range(2,limit) :
    if num_list[i] :
        for j in range(i*2,max,i) :
            num_list[j] = False
result = 0

input()
input_list = list(map(int,input().rstrip().split()))
for num in input_list :
    if num_list[num] :
        result +=1

sys.stdout.write(str(result))